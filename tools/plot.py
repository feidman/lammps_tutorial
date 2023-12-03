#!/usr/bin/env python

# Script:  plot.py
# Purpose: create a simple plot via matplotlib
#          inputs a text file with numbers in columns, suitable for plotting
#          can save it as PNG or PDF file after plot displays
# Syntax:  plot.py infile 1,2 1,4,Press ...
#          infile = text file with numbers in columns
#          X,Y ... = one or more pairs of comma-separated columns to plot
#            first number is X-axis, second number is Y-axis
#            optionally include a 3rd string for a label in the plot legend
# Author:  Steve Plimpton (Sandia), sjplimp at sandia.gov

import sys,os
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 3:
  raise Exception("Syntax: plot.py infile 1,2 ...")

datafile = sys.argv[1]
pairs = sys.argv[2:]

# read the data file
# create Numpy array

data = open(datafile,'r').read().strip()
lines = data.split('\n')

if not len(lines):
  raise Exception("No data in infile")

nrows = len(lines)
ncols = len(lines[0].split())

array = np.zeros((nrows,ncols))

for i,line in enumerate(lines):
  vec = [float(value) for value in line.split()]
  array[i,:] = vec[:]
  
# create the plot

colors = "rgbcmyk"
pairstr = ""

for i,pair in enumerate(pairs):
  if len(pair.split(',')) == 2:
    xcol,ycol = [int(value)-1 for value in pair.split(',')]
    label = "col %d" % (ycol+1)
  elif len(pair.split(',')) == 3:
    xcol,ycol = [int(value)-1 for value in pair.split(',')[:2]]
    label = pair.split(',')[2]
  else:
    raise Exception("No comma in pair of columns")
  pairstr += "%d,%d " % (xcol+1,ycol+1)
  format = colors[i % len(colors)] + "o-"
  plt.plot(array[:,xcol],array[:,ycol],format,label=label)

title = "Columns " + pairstr
plt.title(title)
plt.xlabel("X")
plt.ylabel("Y")

plt.legend()
plt.show()