Tasks for Exercise viz

Goals: Open OVITO with a trajectory generated from previous LAMMPS simulations,
explore the graphical user interface of OVITO, manipulate the data to generate
additonal analysis of the run, create and save a visually impressive image
that is uniquely yours.

One of the best ways to understand a simulation is to inspect what happened
visually, having a visualization tool like OVITO on hand is essential
to doing great science with LAMMPS.

Unlike the LAMMPS examples/demos covered previously in this workshop, we will
be working with a graphical user interface with OVITO, which hopefully is more
intuitive and allows for more user-driven exploration of the tool.

Of note is that your original data is never modified by things you add/modify
within OVITO, so you wont need to rerun your simulation again to reset your
visualization.

-------------------
-------------------

(1) Open the client, load a locally stored trajectory file, save the scene you
have created.

(From the terminal window)
% cd tutorial/demo_viz
% /Path/to/OVITO/bin/ovito

(Now in OVIO graphical interface)
% Load File (Icon in top left, or File -> Load File ) dump.friction from earlier

OVITO auto-interprets many file types, including LAMMPS dump and LAMMPS data.
Additional file types are recognized, many of which do not originate form LAMMPS.
The per-atom data stored as columns in the dump file should be auto-mapped, but
you can adjust or rename the properties by clicking on 'dump.friction' under
'Data Source' on the right hand side, then scrolling down to 'Edit Column Mapping'

% Save a Scene File (Icon in top left, or File -> Save Session State)

This will store which trajectory file(s) have been loaded in, the modifications
made and renedering settings. Very handy when assembling complex graphics.

-------------------

Working with the 'dump.friction' trajectory file.

(2) Change the size of the particles

(3) Change the color of the particles

(4) Add the 'Atomic Strain' modification
      -Set cutoff range to 5
      -Use Frame Number = 0 for the reference configuration.
      (This will compute the strain relative to the starting frame. A strain
      rate per atom can be calculated by setting a relative frame
      reference i.e. -1)
(5) Color atoms with the Shear Strain property, adjust End value to create
something visually interesting.

(6) Render the final state of the simulation, saving the image in tutorial/demo_viz/

Save your progress for later tinkering.

-------------------

(7) Load in the trajectory file from the obstacle example, dump.obstacle
(8) Color atoms by their velocity in the flow direction, adjust ranges.
(9) Create a selecton that captures only the mobile atoms
(10) Create trajectory lines for selected atoms, only generate lines for the
second half of the simulated time
(11) Create a histogram of the flow velocities, of only mobile particles.
(12) Disable visulaization of particles and simulation cell, leaving only
trajectory lines
(13) Clear selection and save your progress

-------------------

(14) Continue with the obstacle example. Replicate the system along the flow
direction 3 times.
(15) Delete mobile particles with a velocity less than zero
(16) Export the remaining atoms to a LAMMPS data file (File -> Export file)

You can now load this data file as the starting point to a new simulation.
This demonstrates the possibility to generate complex initial structures from
OVITO, and doing so through a graphical interface.
