#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch

## Read places data file 
pl_arr = []
fp = open ('places.csv', 'r')
for line in fp:
	line = line.strip('\n').strip()
	line = line.split(',')
	pl_arr.append(line)
fp.close()

print len(pl_arr)
#print (pl)
#for i in len(pl_arr):
#	print (pl_arr[i])