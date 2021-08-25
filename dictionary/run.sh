#!/bin/bash

# we only need MSYS_NO_PATHCONV when running this script in Windows
# because otherwise Mingw will try to convert
# the given paths and that breaks everything.
MSYS_NO_PATHCONV=1 docker run --rm -p 8080:8080 -v "${PWD}/default":"/etc/fancify/dictionary" fancify-dictionary:latest
