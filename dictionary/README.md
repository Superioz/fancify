# fancify-dictionary

This service is for fetching nouns and adjectives from different sources, like flat files, and exposing them as a service for other services or clients.

Inside the `default` folder are the default `sources.yml` config and the dictionary files `nouns.json` and `adjectives.json` for easy deployment. If you want to use different files, you have to match the data format from these files.

# Manual setup

- `pip3 install .`
- `python3 main.py`

Wow.

# Routes

- `GET /nouns` with parameters `size` and `page`
- `GET /adjectives` with parameters just like nouns has
