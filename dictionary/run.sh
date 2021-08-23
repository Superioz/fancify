#!/bin/bash
docker run --rm -p 8080:8080 -v "/${PWD}/default":"/etc/fancify/dictionary/" fancify-dictionary:latest
