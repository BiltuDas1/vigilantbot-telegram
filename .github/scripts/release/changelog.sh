#!/bin/bash
# Full version with version type
FullVer=$(cat version.txt)

# Get old version from CHANGELOG.md
OLD_FullVer=$(grep -i -o1 "^## \[\(.\+\)\]" CHANGELOG.md | head -2 | tail -1 | cut -d\[ -f2 | cut -d\] -f1)

# Updates the CHANGELOG.md if version.txt version information doesn't avaliable into the CHANGELOG.md
if ! grep -c "\[$FullVer\]" CHANGELOG.md >/dev/null; then
    # Replaces the unreleased version with compared url
    if [[ "$OLD_FullVer" == "unreleased" ]]; then
        sed -i -e 's/\[unreleased\]: https:\/\/github.com\/BiltuDas1\/vigilantbot-telegram/\['$FullVer'\]: https:\/\/github.com\/BiltuDas1\/vigilantbot-telegram\/tree\/'$FullVer'/' CHANGELOG.md
    else
        sed -i -e 's/\[unreleased\]: https:\/\/github.com\/BiltuDas1\/vigilantbot-telegram\/compare\/'$OLD_FullVer'...main/\['$FullVer'\]: https:\/\/github.com\/BiltuDas1\/vigilantbot-telegram\/compare\/'$OLD_FullVer'...'$FullVer'/' CHANGELOG.md
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
    echo \[unreleased\]: https://github.com/BiltuDas1/vigilantbot-telegram/compare/$FullVer...main >> CHANGELOG.md.swap

    # Remove the old changelog and replace it with new one
    rm CHANGELOG.md
    mv CHANGELOG.md.swap CHANGELOG.md
fi

















    # fp=$(grep -n "##" CHANGELOG.md | head -1 | cut -f1 -d:)
    
    # cat CHANGELOG.md | head -$((fp-1)) > CHANGELOG.md.swap
    # echo \#\# \[unreleased\] >> CHANGELOG.md.swap
    # echo - There\'s Nothing but Crickets ¯\\\\_\(ツ\)_/¯ >> CHANGELOG.md.swap
    # echo >> CHANGELOG.md.swap

    # sp=$(grep -n "\-\-\-" CHANGELOG.md | cut -f1 -d:)
    # cat CHANGELOG.md | head -$sp | tail +$fp >> CHANGELOG.md.swap
    # echo >> CHANGELOG.md.swap
    # echo \[unreleased\]: https://github.com/BiltuDas1/qsort/compare/$VER...pre/beta >> CHANGELOG.md.swap
    # cat CHANGELOG.md | tail +$((sp+2)) >> CHANGELOG.md.swap