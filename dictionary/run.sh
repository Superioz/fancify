#!/bin/bash

IMAGE="fancify-dictionary:latest"

# Check if the image is present on this machine
# If not, we build it ourselves
if !(docker image inspect $IMAGE &> /dev/null) || [[ $1 == "--rebuild" ]]; then
    echo "Image $IMAGE is not present, building it .."
    docker build -t $IMAGE .
fi

# we only need MSYS_NO_PATHCONV when running this script in Windows
# because otherwise Mingw will try to convert
# the given paths and that breaks everything.
MSYS_NO_PATHCONV=1 docker run -it --rm -p 8080:8080 -v "${PWD}/default":"/etc/fancify/dictionary" $IMAGE
