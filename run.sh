#!/bin/bash

pip install -r src/requirements.txt
export PYTHONPATH=$(pwd)
echo $PYTHONPATH
python src/main.py