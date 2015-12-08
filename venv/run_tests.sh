#!/bin/bash

set -e  # If occur any error, exit
function to_console {
    echo -e "\n $1 \n"
}


virtualenv venv/
echo ""
echo " --> Created the Virtualenv."

source venv/bin/activate
echo ""
echo " --> Activated the Virtualenv."
echo ""

pip install -r venv/requirements.txt
echo ""
echo " --> Installed the requirements."
echo ""

python tests/run_tests.py

to_console " --> Ran the tests in tests/run_tests.py"