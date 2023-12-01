#!/bin/bash
Ver=$(cat version.txt)
build_date=$(date +%F)

# Editing Version information in Dockerfile
sed -i -r 's/^LABEL version="(.?)+"$/LABEL version="'$Ver'"/' Dockerfile

# Editing Build date information in Dockerfile
sed -i -r 's/^LABEL build_date="(.?)+"$/LABEL build_date="'$build_date'"/' Dockerfile