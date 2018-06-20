# GitLab CHANGELOG Generator

[![Build Status](https://travis-ci.org/stuartmccoll/gitlab-changelog-generator.svg?branch=master)](https://travis-ci.org/stuartmccoll/gitlab-changelog-generator) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

A simple command line utility to produce a CHANGELOG.md file from the commit differences between two GitLab project branches.

**Python 3.6** is required to run this utility.

## Installation

This utility can be installed through [pip](https://pypi.org/project/pip/) by running the following command:

```shell
pip install gitlab-changelog-generator
```

## Usage

```shell
changegen --ip localhost --group test-projects --project test-project --branches master release --version 1.1
```

## Tests

Tests for this project utilise the [Pytest](https://pypi.org/project/pytest/) framework. To run the existing suite of unit tests run the following command within the root directory:

```shell
pytest
```

## Notes

All Python code has been formatted by [Black](https://github.com/ambv/black), 'the uncompromising Python code formatter'.

Type checking has been provided by [Pyre](https://pyre-check.org/).

Continuous integration is handled by [Travis CI](https://travis-ci.org/).

## License

See [LICENSE.md](LICENSE.md).