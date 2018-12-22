import pkg_resources
import json
import sys
import random
import string
from api import idfancy

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
    noun = idfancy.Noun(s["noun"], s["article"])
    nouns.append(noun)
sorted(nouns)

# get the id to be converted
ids = sys.argv[1:]

if len(ids) == 0:
    print("As you didn't pass an id let's generate a new id ..")
    ids.append("".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=8)))
else:
    print("You passed %d ids .." % len(ids))

# get the converted words
words = idfancy.process_ids(ids, adjectives, nouns)

# print out the results
print("\nId           Conversion")
for _id in words:
    print("%s     '%s'" % (_id, str(words[_id])))
