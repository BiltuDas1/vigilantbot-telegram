## [unreleased]
- Changed: Now the docker image uses Python 3.9 as base image

## [0.1.4-alpha] - 2023-12-01
- Fixed: Github actions now will generate docker image with version information and version type
- Fixed: Now Github release will included version type along with version
- Now docker image is available with the following architectures: linux/386, linux/amd64, linux/arm/v7, linux/arm64/v8, linux/arm/v6

## [0.1.3-alpha] - 2023-12-01
- Fixed: Now github action will also generate docker image for arm64
- Removed additional 'Installing requirements...' message at the startup of the script

## [0.1.2-alpha] - 2023-11-29
- Fixed: Dockerfile version and build date is not changing

## [0.1.1-alpha] - 2023-11-29
- Fixed Dockerfile
- Updated automatic building docker images in Github Actions
- Now users can set custom webapp Port by using the `PORT` Environment Variable in .env

## [0.1.0-alpha] - 2023-11-27
- Added nudity filter using [Nudenet](https://pypi.org/project/nudenet/) python library

## [0.0.2-alpha] - 2023-11-27
- Updated Documentation

## [0.0.1-alpha] - 2023-11-27
- Added bot required permission checker
- Added [SpamWatch API](https://github.com/SpamWatch) to filter user

---
[0.0.1-alpha]: https://github.com/BiltuDas1/vigilantbot-telegram/tree/0.0.1
[0.0.2-alpha]: https://github.com/BiltuDas1/vigilantbot-telegram/compare/0.0.1...0.0.2
[0.1.0-alpha]: https://github.com/BiltuDas1/vigilantbot-telegram/compare/0.0.2...0.1.0
[0.1.1-alpha]: https://github.com/BiltuDas1/vigilantbot-telegram/compare/0.1.0...main
[0.1.2-alpha]: https://github.com/BiltuDas1/vigilantbot-telegram/compare/0.1.1...0.1.2
[0.1.3-alpha] - 2023-12-01: https://github.com/BiltuDas1/vigilantbot-telegram/compare/0.1.2...main
[0.1.4-alpha] - 2023-12-01: https://github.com/BiltuDas1/vigilantbot-telegram/compare/0.1.3...main
[unreleased]: https://github.com/BiltuDas1/vigilantbot-telegram/compare/0.1.4...main
