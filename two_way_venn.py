#!/usr/bin/python

#Usage: python venn.py <group1Count> <group2Count> <bothCount> <outFile>

import sys

from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles
from matplotlib_venn import venn2
import matplotlib as mpl

mpl.rc('font', family='Arial')

group1 = int(sys.argv[1])
group2 = int(sys.argv[2])
both = int(sys.argv[3])
outfile = sys.argv[4]

plt.figure(figsize=(8,8))
plt.figure(dpi=1000)
venn2(subsets = (group1, group2, both), set_labels = ('group1', 'group2'), set_colors=('b', 'r') )

plt.savefig(outfile, format='pdf')

