#!/usr/bin/env python
"""
	run_ocr.py
"""

import os
import easyocr
import numpy as np
import pandas as pd
from glob import glob
from tqdm import tqdm

np.set_printoptions(linewidth=120)

# --
# Run OCR

reader = easyocr.Reader(['en','en'])

indir = 'results/2022_12'
out   = {}
for fname in tqdm(os.listdir(indir)):
	inpath = os.path.join(indir, fname)
	result = reader.readtext(inpath, min_size=2)
	out[fname.split('.')[0]] = [xx[-2] for xx in result]

# --
# Inspect results

field_names = pd.read_excel('data/field_names.xlsx', header=None, engine='openpyxl')
field_names = field_names.values

data    = field_names.copy()
data[:] = ''

for k,v in out.items():
	if len(v) == 0: continue
	r, c = np.where(field_names == k)
	r, c = int(r), int(c)
	data[r, c] = ' '.join(v)

df = pd.DataFrame(data)
df.to_csv('data/boxscores.csv')


