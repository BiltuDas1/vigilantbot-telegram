#!/bin/bash
Ver=$(cat version.txt)
Version=$(echo $Ver | cut -f1 -d-)
VersionType=$(echo $Ver | cut -f2 -d-)

echo "Version=$Version" >> $GITHUB_ENV

if [[ $VersionType == "beta" ]]; then
    echo "Prerelease=true" >> $GITHUB_ENV
else
    echo "Prerelease=false" >> $GITHUB_ENV
fi