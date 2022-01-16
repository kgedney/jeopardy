#!/bin/bash

# run.sh

# --
# Setup environment

conda create -y -n jeopardy_env python=3.7
conda activate jeopardy_env

pip install labelImg
pip install matplotlib
pip install pandas
pip install openpyxl
pip install git+https://github.com/bkj/rcode
