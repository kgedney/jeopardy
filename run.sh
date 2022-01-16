#!/bin/bash

# run.sh

# --
# Download data

./data.sh

# --
# Extract chips

python extract_chips.py --inpath data/2022_12.jpg
python extract_chips.py --inpath data/2022_13.jpg
python extract_chips.py --inpath data/2022_14.jpg