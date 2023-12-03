Here is the list of tools we will use during the LAMMPS tutorial:

available text editors:
  emacs, vi, vim
  use whichever one is familiar to you

lmp = LAMMPS executable
log2txt.py = Python script to extract thermodynamic data from a LAMMPS logfile
plot.py = Python script to plot columns of logfile data
eom = visualize an image file
vlc = play an MPG movie
evince = PDF file viewer
ovito = Ovito visualization package

-----------

The tooltest dir has data files to let you try out all of these tools.
Please do this BEFORE the tutorial, so you are familiar with how to
use them.

This simulation is a simple 2d model of small polar molecules forming
micelles in background fluid.

Here are the commands to type:

% cd tooltest

% lmp < in.micelle                  # run a short LAMMPS simulation
                                    # this produces all the other files
                                    # except plot.pdf
% log2txt.py log.lammps data.txt    # create data.txt with columns of numbers
% plot.py data.txt 1,2 1,4          # plot 2 columns from data.txt
% plot.py data.txt 1,2,Temp 1,4,Emol    # ditto with curve labels
% eom image.00000.jpg               # view first and last snapshots of atoms
% eom image.50000.jpg
% eom image*                        # view all the snapshots
% vlc movie.mpg                     # play a movie of the simulation
% evince plot.pdf                   # display a saved plot file
% ovito dump.micelle                # open Ovito with a LAMMPS dump file
                                    # or click on the Ovito icon to launch

Try out your text editor of choice:

% emacs in.micelle                  # open LAMMPS input script in a text editor
% vi in.micelle
% vim in.micelle

-----------

Here is more info on how to use the 2 Python script tools:

Syntax for log2txt.py tool:
  log2txt.py logfile datafile col1 col2 ...
  logfile = name of the LAMMPS log file
  datafile = name of text data file to produce
  col1, col2, ... = optional column names to extract
    see the line in the LAMMPS logfile that starts with "Step ..."
      to see the column names
    e.g. Step E_pair Press Volume
  if col* args are not used, all columns are extracted
  if 3 col args are used, the datafile will have 3 columns of numbers

Syntax for plot.py tool:
  plot.py datafile X1,Y1 X2,Y2,Name ...
  datafile = name of text file to plot data from
  X1,Y1 = 2 integers separated by a comma or
          2 integers and a string separated by commas
          repeated as many times as desired
    each set of comma-separated arguments is a curve to plot
    1,3 means x-axis is column 1, y-axis is column 3
    the optional Name string will appear in the plot legend
  add as many curves to the same plot as you wish
  the plot will have a legend labeled by Y1, Y2, etc or the Names
  when the plot displays, you can click the disc icon at the bottom,
    to save the plot as a PNG or PDF file and give it a name,
    which can later be viewed with the "eom" or "evince" tool
