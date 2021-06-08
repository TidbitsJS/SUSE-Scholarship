#!/bin/sh

## main script to be executed by Flask
export FLASK_APP=./cashman/index.py

## activated the virtual environment created by pipenv
source $(pipenv --venv)/bin/activate

## Run application
flask run -h 0.0.0.0

