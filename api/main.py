from flask import Flask, request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from os import getenv
import sys
import requests
import random


class Noun:
    """Represents a noun with its respective article."""

    def __init__(self, noun, article):
        self.noun = noun
        self.article = article


def fancify_content(content, nouns, adjectives):
    """
    Method to hash the content for a random number generator
    seed and get the respective noun and adjective.

    Returns a string like `der alte Vater`
    """
    random.seed(content)
    noun = nouns[random.randint(0, len(nouns) - 1)]
    adjective = adjectives[random.randint(0, len(adjectives) - 1)]

    return noun.article + " " + adjective + " " + noun.noun


dictionary_address = getenv(
    "FANCIFY_DICTIONARY_ADDRESS", default="http://localhost:8080")


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
    return r.json()


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
# if we can't connect to the service, we just exit.
print("Load lexicon into cache ...")
adjectives = fetch_adjectives()
if adjectives == None:
    print("Could not load any adjectives, exiting ..")
    exit(1)
print(f"Loaded {len(adjectives)} adjectives")

nouns = fetch_nouns()
if nouns == None:
    print("Could not load any nouns, exiting ..")
    exit(1)
print(f"Loaded {len(nouns)} nouns")

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

    if "content" not in data:
        return jsonify(status="body needs to contain field 'content'"), 400
    content = data["content"]

    return jsonify(result=fancify_content(content, nouns, adjectives)), 200


if __name__ == "__main__":
    app.run(host=getenv("SERVER_HOST", default="0.0.0.0"),
            port=getenv("SERVER_PORT", default="8090"))
