import re
import random


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


def process_ids(ids, adjectives, nouns):
    generated_words = {}
    for _id in ids:
        real_id, word = _process_id(_id, adjectives, nouns)

        if word is not None:
            generated_words[real_id] = word
    return generated_words


def _process_id(_id, adjectives, nouns):
    # check if the id matches the specific pattern
    id_pattern = re.compile("^[a-zA-Z0-9]{8}$")
    link_pattern = re.compile("^(http://)?game.rewinside.tv/([a-zA-Z0-9]{8})$")

    real_id = _id
    if link_pattern.match(_id):
        real_id = _id.split("tv/")[1]

    if not id_pattern.match(real_id):
        return real_id, None

    # hashes the id and turns it into a random combination
    # of adjectives and nouns
    random.seed(real_id)
    word = FancyWord(nouns[random.randint(0, len(nouns) - 1)], adjectives[random.randint(0, len(adjectives) - 1)])

    # final word, yay
    return real_id, word
