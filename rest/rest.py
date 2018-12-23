import pkg_resources
import json
from flask import Flask, request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from api import idfancy

# initialize Flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["24000 per day", "1000 per hour"]
)

# fetch the nouns and adjectives from this package
package = "dictionary"

nouns_path = "/".join(("../" + package, "nouns.json"))
adjectives_path = "/".join(("../" + package, "adjectives.json"))

# load the json content of the files
nouns_json = json.loads(pkg_resources.resource_string(__name__, nouns_path))
adjectives = json.loads(pkg_resources.resource_string(__name__, adjectives_path))
sorted(adjectives)

# put all nouns into a list.
# the adjectives are already in a list
nouns = []
for s in nouns_json:
    noun = idfancy.Noun(s["noun"], s["article"])
    nouns.append(noun)
sorted(nouns)


@app.errorhandler(400)
def bad_request(_):
    return jsonify(status="bruder mach nicht diese", code=400)


@app.errorhandler(405)
def method_not_allowed(_):
    return jsonify(status="ja nu komm", code=405)


@app.errorhandler(404)
def file_not_found(_):
    return jsonify(status="freunde, bitte", code=404)


@app.errorhandler(429)
def too_many_requests(_):
    return jsonify(status="freunde, beruhigt euch", code=429)


@app.errorhandler(500)
def internal_error(_):
    return jsonify(status="isch hab ruecken, isch hab kreislauf", code=500)


@app.route("/ping")
@limiter.exempt
def ping():
    return jsonify(status=":^)")


@app.route("/", methods=["POST"])
def fancify():
    data = request.get_json()
    if data is None or isinstance(data, int):
        return jsonify(status="bruder mach nicht diese", code=400)

    keys = []
    for _id in data:
        keys.append(str(_id))

    # process given input and return the processed ids
    # or empty if no valid id found
    words = idfancy.process_ids(keys, adjectives, nouns)
    results = {}
    for _id in words:
        results[_id] = str(words[_id])

    return jsonify(status="ok", data=results), 200


@app.route("/")
def test():
    return render_template("index.html")


# start the web service
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1337)
