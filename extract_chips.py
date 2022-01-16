#!/usr/bin/env python

"""
  grid.py
"""

import os
import sys
import argparse
import numpy as np
import pandas as pd
from PIL import Image

from rcode import *
from matplotlib import pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

# --
# CLI

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inpath', type=str, default='data/2022_12.jpg')
    parser.add_argument('--outdir', type=str, default='results')
    args = parser.parse_args()
    
    args.outdir = os.path.join(args.outdir, os.path.basename(args.inpath).split('.')[0])
    
    return args

args = parse_args()

os.makedirs(args.outdir, exist_ok=True)

# --
# IO

img         = Image.open(args.inpath)
field_names = pd.read_excel('data/field_names.xlsx', header=None).values

# --
# Grid lines

vlines = [0, 250, 425, 600, 800, 1000, 1225, 1400, 1525, 1700, 1850, 1920]

hlines = [
  0,
  185, 235, 265, 315, 
  360, 410, 440, 490, 
  550, 600, 630, 680,
  725, 775, 805, 855,
  910, 975,
  1080
]

# --
# Extract chips

img = np.asarray(img)

for c in range(len(vlines) - 1):
  for r in range(len(hlines) - 1):
    
    field_name = field_names[r, c]
    if field_name == 'None': continue
    
    c_start, c_stop = vlines[c], vlines[c + 1]
    r_start, r_stop = hlines[r], hlines[r + 1]
    
    chip    = img[r_start:r_stop, c_start:c_stop]
    outpath = f'{args.outdir}/{field_names[r, c]}.png'
    Image.fromarray(chip).save(outpath)

