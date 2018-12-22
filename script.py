import pkg_resources
import json
import sys
import re
import random
import string


class Noun:
    def __init__(self, no, article):
        self.noun = no
        self.article = article

    def __lt__(self, other):
        return self.noun < other.noun


class FancyWord:
    def __init__(self, no, adj):
        self.no = no
        self.adj = adj

    def __str__(self):
        return self.no.article + " " + self.adj + " " + self.no.noun


# fetch the nouns and adjectives from this package
package = "dictionary"

nouns_path = "/".join((package, "nouns.json"))
adjectives_path = "/".join((package, "adjectives.json"))

# load the json content of the files
nouns_json = json.loads(pkg_resources.resource_string(__name__, nouns_path))
adjectives = json.loads(pkg_resources.resource_string(__name__, adjectives_path))
sorted(adjectives)

# put all nouns into a list.
# the adjectives are already in a list
nouns = []
for s in nouns_json:
    noun = Noun(s["noun"], s["article"])
    nouns.append(noun)
sorted(nouns)

# get the id to be converted
ids = sys.argv[1:]

if len(ids) == 0:
    print("As you didn't pass an id let's generate a new id ..")
    ids.append("".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=8)))
else:
    print("You passed %d ids .." % len(ids))


def _process_id(_id):
    # check if the id matches the specific pattern
    id_pattern = re.compile("^[a-zA-Z0-9]{8}$")
    link_pattern = re.compile("^(http://)?game.rewinside.tv/([a-zA-Z0-9]{8})$")

    real_id = _id
    if link_pattern.match(_id):
        real_id = _id.split("tv/")[1]

    if not id_pattern.match(real_id):
        print("id doesn't match the pattern: %s" % real_id)
        quit()

    # hashes the id and turns it into a random combination
    # of adjectives and nouns
    random.seed(real_id)
    word = FancyWord(nouns[random.randint(0, len(nouns) - 1)], adjectives[random.randint(0, len(adjectives) - 1)])

    # final word, yay
    return real_id, word


# print out the results
print("\nId           Conversion")
for _id in ids:
    _real_id, _word = _process_id(_id)
    print("%s     '%s'" % (_real_id, str(_word)))
