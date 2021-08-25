from flask import Flask, request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from os import getenv
import sys
import requests


class Noun:
    """Represents a noun with its respective article."""

    def __init__(self, noun, article):
        self.noun = noun
        self.article = article


dictionary_address = getenv(
    "FANCIFY_DICTIONARY_ADDRESS", default="http://localhost:8080")


def fancify_content(content, nouns, adjectives):
    return content


def fetch_adjectives():
    print("Fetch adjectives ...")
    r = None
    try:
        r = requests.get(f"{dictionary_address}/adjectives")
        if r.status_code != 200:
            return None
    except Exception as e:
        print("Could not connect to dictionary service:", e)
        return None
    return r.text


def fetch_nouns():
    print("Fetch nouns ...")
    r = None
    try:
        r = requests.get(f"{dictionary_address}/nouns")
        if r.status_code != 200:
            return None
    except Exception as e:
        print("Could not connect to dictionary service:", e)
        return None

    nouns = []
    for n in r.json():
        nouns.append(Noun(n["noun"], n["article"]))
    return nouns


# connect to dictionary service and fetch all adjectives and nouns
# save them into a cache that gets cleared every x minutes
print("Load lexicon into cache ...")
adjectives = fetch_adjectives()
print(f"Loaded {len(adjectives)} adjectives")
nouns = fetch_nouns()
print(f"Loaded {len(nouns)} nouns")

if adjectives == None or nouns == None:
    print("Could not find anything for the lexicon, exiting ..")
    exit(1)

app = Flask("fancify-api")
app.config['JSON_AS_ASCII'] = False
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5000 per hour"]
)


@app.route("/fancify", methods=["POST"])
def fancify():
    data = request.json
    if data == None:
        return jsonify(status="the body needs to be json encoded"), 400

    content = data["content"]
    if content == None:
        return jsonify(status="body needs to contain field 'content'"), 400

    return jsonify(result=fancify_content(content, nouns, adjectives)), 200


if __name__ == "__main__":
    app.run(host=getenv("SERVER_HOST", default="0.0.0.0"),
            port=getenv("SERVER_PORT", default="8090"))
