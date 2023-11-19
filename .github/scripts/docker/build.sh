#!/bin/bash
USER=$1
Ver=$(cat version.txt)
VERSION=$(echo $Ver | cut -f1 -d-)
LATEST=$(docker pull $USER/vigilantbot -a | cut -d: -f1 | head -1 | tail -1)

if [[ $VERSION != $LATEST ]]; then
    # Building docker image
    docker build -t $USER/vigilantbot:latest .
    docker tag $USER/vigilantbot:latest $USER/vigilantbot:$VERSION

    # Pushing to docker hub
    docker push -a $USER/vigilantbot
else
    echo "Already on latest version"
fi