# fancify-api

This is the main service for the Fancify application. It connects to the dictionary service and exposes a route to fancify any content.

# Manual setup

- `pip3 install .`
- `python3 main.py`

Wow.

# Routes

- `POST /fancify`: With a body like `{ "content": "your string" }`, will return the fancified content.

# Environment Variables

- `SERVER_HOST`: Host this application will bind to.
- `SERVER_PORT`: Port this application will bind to.
- `FANCIFY_DICTIONARY_ADDRESS`: Address of the dictionary service. Needs to have the format `http://host:port`
