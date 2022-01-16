#!/usr/bin/env python

"""
  plot_grid.py
"""

#!/usr/bin/env python

"""
  grid.py
"""

import os
from PIL import Image

from rcode import *
from matplotlib import pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

# --
# IO

img         = Image.open('data/2022_12.jpg')

# --

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

def do_plot():
  fig, ax = plt.subplots(figsize=(10, 8))
  ax.xaxis.set_major_locator(MultipleLocator(50))
  ax.yaxis.set_major_locator(MultipleLocator(50))
  for tick in ax.get_xticklabels():
      tick.set_rotation(45)
  
  _ = ax.imshow(img)
  
  for v in vlines:
    _ = plt.axvline(v, c='red')
  
  for v in hlines:
    _ = plt.axhline(v, c='red')
  
  # _ = plt.grid('both')
  plt.savefig('grid.png')

do_plot()