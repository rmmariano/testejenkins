#!/bin/bash

virtualenv venv/
echo ""
echo " --> Created the VirtualEnv in venv/"

source venv/bin/activate
echo ""
echo " --> Activated the VirtualEnv in venv/"
echo ""

pip install -r venv/requirements.txt
echo ""
echo " --> Installed the requirements in venv/"
echo ""

python tests/run_tests.py
echo ""
echo " --> Ran the tests in tests/run_tests.py"

deactivate
echo ""
echo " --> Deactivated the VirtualEnv in venv/\n"
echo ""