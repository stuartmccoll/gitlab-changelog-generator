# GitLab CHANGELOG Generator

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

A simple command line utility to produce a CHANGELOG.md file from the commit differences between two GitLab project branches.

## Installation

This utility can be installed through [pip]() by running the following command:

```shell
pip install gitlab-changelog-generator
```

## Usage

```shell
changegen --ip localhost --group test-projects --project test-project --branches master release --version 1.1
```

## Notes

All Python code has been formatted by [Black](https://github.com/ambv/black), 'the uncompromising Python code formatter'.

Type checking has been provided by [Pyre](https://pyre-check.org/).

## License

See [LICENSE.md](LICENSE.md).