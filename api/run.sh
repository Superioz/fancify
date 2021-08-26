#!/bin/bash

IMAGE="fancify-api:latest"

# Check if the image is present on this machine
# If not, we build it ourselves
if !(docker image inspect $IMAGE &> /dev/null) || [[ $1 == "--rebuild" ]]; then
    echo "Image $IMAGE is not present, building it .."
    docker build -t $IMAGE .
fi

docker run -it --rm -p 8090:8090 --env FANCIFY_DICTIONARY_ADDRESS=http://host.docker.internal:8080 $IMAGE
