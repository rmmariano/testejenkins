#!/bin/bash

virtualenv venv/

source venv/bin/activate

pip install -r venv/requirements.txt

python tests/run_tests.py

deactivate
