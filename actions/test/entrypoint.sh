#!/bin/sh -l

sh -c "echo 'Running unit tests...'"

ls
pip install -e .
pytest