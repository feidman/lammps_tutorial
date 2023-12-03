#!/usr/bin/env python

# Script:  log2txt.py
# Purpose: extract thermo info from LAMMPS log file
#          create a text file of numbers in columns, suitable for plotting
# Syntax:  log2txt.py log.lammps data.txt X Y ...
#          log.lammps = LAMMPS log file
#          data.txt = text file to create
#          X Y ... = columns to include (optional), X,Y are thermo keywords
#                    if no columns listed, all columns are included
# Author:  Steve Plimpton (Sandia), sjplimp at sandia.gov

import sys,os
from log import log

if len(sys.argv) < 3:
  raise Exception("Syntax: log2txt.py log.lammps data.txt X Y ...")

logfile = sys.argv[1]
datafile = sys.argv[2]
columns = sys.argv[3:]

lg = log(logfile)
lg.write(datafile,*columns)