#!/bin/bash
# Full version with version type
FullVer=$(cat version.txt)
PartialVer=$(echo $FullVer | cut -f1 -d-)

# Get old version from CHANGELOG.md
OLD_FullVer=$(grep -i -o1 "^## \[\(.\+\)\]" CHANGELOG.md | head -2 | tail -1 | cut -d\[ -f2 | cut -d\] -f1)
OLD_PartialVer=$(echo $OLD_FullVer | cut -f1 -d-)

result=$(grep -c "\[$FullVer\]" CHANGELOG.md)
# Updates the CHANGELOG.md if version.txt version information doesn't avaliable into the CHANGELOG.md
if [[ $result -eq 0 ]]; then
    # Replaces the unreleased version with compared url
    if [[ "$OLD_FullVer" == "unreleased" ]]; then
        sed -i -e 's/\[unreleased\]: https:\/\/github.com\/BiltuDas1\/vigilantbot-telegram/\['$FullVer'\]: https:\/\/github.com\/BiltuDas1\/vigilantbot-telegram\/tree\/'$PartialVer'/' CHANGELOG.md
    else
        sed -i -e 's/\[unreleased\]: https:\/\/github.com\/BiltuDas1\/vigilantbot-telegram\/compare\/'$OLD_PartialVer'...main/\['$FullVer'\]: https:\/\/github.com\/BiltuDas1\/vigilantbot-telegram\/compare\/'$OLD_PartialVer'...'$PartialVer'/' CHANGELOG.md
    fi

    # Adds the version no and release date to unreleased version
    sed -i 's/\[unreleased\]/\['$FullVer'\] - '$(date +%F)'/' CHANGELOG.md

    # Add unreleased section
    (
        echo \#\# \[unreleased\] &&
        echo There\'s Nothing but Crickets ¯\\\\_\(ツ\)_/¯ &&
        echo &&
        cat CHANGELOG.md
    ) > CHANGELOG.md.swap

    # Linking unrelease version with compare url
    echo \[unreleased\]: https://github.com/BiltuDas1/vigilantbot-telegram/compare/$PartialVer...main >> CHANGELOG.md.swap

    # Remove the old changelog and replace it with new one
    rm CHANGELOG.md
    mv CHANGELOG.md.swap CHANGELOG.md
fi
