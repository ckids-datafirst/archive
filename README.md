# datafest-archive

<div align="center">

[![Build status](https://github.com/ckids-datafirst/archive/workflows/build/badge.svg?branch=master&event=push)](https://github.com/ckids-datafirst/archive/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/datafest-archive.svg)](https://pypi.org/project/datafest-archive/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/ckids-datafirst/archive/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/ckids-datafirst/archive/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/ckids-datafirst/archive/releases)
[![License](https://img.shields.io/github/license/ckids-datafirst/archive)](https://github.com/ckids-datafirst/archive/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

</div>

DataFestArchive is a Python package designed to generate the DataFestArchive website from past versions of DataFest

## Installation

```bash
git clone https://github.com/ckids-datafirst/archive.git
poetry run datafest-archive --help
```

## Usage

```bash
$ poetry run datafest-archive generate --help

 Usage: datafest-archive generate [OPTIONS] INPUT_PATH WEBSITE_OUTPUT_DIRECTORY

Arguments
* path INPUT_PATH  The input path to use. Depends on the type. [default: None] [required]
* website_output_directory PATH The directory to output the website to. [default: None] [required]

Options
* --input-type [json]  The type of website to generate. [default: None] [required]
   --help                      Show this message and exit.
```

### Example

Generate the website from the JSON files in the `datafest-archive/data` directory and output the website to the `datafest-archive/website` directory.

```bash
$ poetry run datafest-archive generate --input-type json --input-path datafest-archive/data --website-output-directory datafest-archive/website
```

The directory structure of the data directory should look like [this example](tests/input_data/json/2022-fall.json)

## Development documentation

Refer to [README-dev.md](README-dev.md) for development documentation.

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/ckids-datafirst/archive/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/ckids-datafirst/archive/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/ckids-datafirst/archive)](https://github.com/ckids-datafirst/archive/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/ckids-datafirst/archive/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{datafest-archive,
  author = {ckids-datafirst},
  title = {DataFestArchive is a Python package designed to generate the DataFestArchive website from past versions of DataFest},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ckids-datafirst/archive}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
