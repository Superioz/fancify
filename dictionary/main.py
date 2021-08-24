from flask import Flask, request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from os import getenv
import yaml
import json


class Noun:
    """Represents a noun with its respective article."""

    def __init__(self, noun, article):
        self.noun = noun
        self.article = article


class Source:
    """
    Represents a source to get the nouns and adjectives from.
    Could be a flat file, a database or a different service.
    """
    supported_types = ["file"]

    def __init__(self, yaml_object):
        self.type = yaml_object["type"]

        if self.type not in self.supported_types:
            print("this type is not supported")

    def get_nouns(self):
        return []

    def get_adjectives(self):
        return []


class FileSource(Source):
    """
    Source to get adjectives and nouns from specific files.
    """
    nouns = None
    adjectives = None

    def __init__(self, yaml_object):
        super().__init__(yaml_object)
        self.nounsFilePath = yaml_object["nounsFile"]
        self.adjectivesFilePath = yaml_object["adjectivesFile"]

    def get_nouns(self):
        if self.nouns is None:
            nouns = []

            with open(self.nounsFilePath, encoding="utf-8") as json_file:
                data = json.load(json_file)
                for n in data:
                    nouns.append(Noun(n["noun"], n["article"]))
            self.nouns = nouns
        return self.nouns

    def get_adjectives(self):
        if self.adjectives is None:
            with open(self.adjectivesFilePath, encoding="utf-8") as json_file:
                data = json.load(json_file)
                self.adjectives = data
        return self.adjectives

    def __repr__(self):
        return self.__dict__.__str__()


def get_source_from(yaml_object):
    """
    Depending on what type the source inside the given
    yaml_object has, this method returns a different kind of
    source.

    If the source type is not supported, this will fail.
    """
    source_type = yaml_object["type"]

    if source_type == "file":
        return FileSource(yaml_object)
    else:
        return Source(yaml_object)


def handle_get_paged_list(list):
    raw_size = request.args.get("size")
    raw_page = request.args.get("page")

    size = int(raw_size) if raw_size != None else len(list)
    page = int(raw_page) if raw_page != None else 1

    if size <= 0:
        return jsonify(status="size less or equal to zero is not allowed"), 400

    paged_list = [list[i:i+size] for i in range(0, len(nouns), size)]
    if page > len(paged_list):
        return jsonify(status=f"this page does not exist ({page} >= {len(paged_list)})"), 400
    return jsonify(paged_list[page-1]), 200


print("Load config ...")

# load config to determine where to search for the
# dictionary sources (the nouns and adjectives)
config_path = getenv("FANCIFY_DICTIONARY_SOURCES_CONFIG",
                     default="/etc/fancify/dictionary/sources.yml")
sources = []
with open(config_path, "r") as stream:
    try:
        config_file = yaml.safe_load(stream)
        raw_sources = config_file["sources"]

        for s in raw_sources:
            sources.append(get_source_from(s))
    except yaml.YAMLError as err:
        print(err)

print(f"Found sources: {sources}")
print("Load lexicon from sources ...")

nouns = []
adjectives = []
for source in sources:
    for n in source.get_nouns():
        nouns.append(n.__dict__)
    adjectives.extend(source.get_adjectives())

print(f"Found {len(nouns)} nouns and {len(adjectives)} adjectives.")

app = Flask("fancify-dictionary")
app.config['JSON_AS_ASCII'] = False
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["24000 per day", "1000 per hour"]
)


@app.route("/nouns")
def get_nouns():
    return handle_get_paged_list(nouns)


@app.route("/adjectives")
def get_adjectives():
    return handle_get_paged_list(adjectives)


if __name__ == "__main__":
    app.run(host=getenv("SERVER_HOST", default="0.0.0.0"),
            port=getenv("SERVER_PORT", default="8080"))
