import numpy as np
import subprocess
import shlex
import glob, os
import time

start_time = time.time()

j = 0
x = []
y = []
target = "%%"

for i in list(np.arange(3.00, 5.05, 0.10)):
    command_line = f'\"/opt/lammps-3Nov2022/build_most/lmp\" \
            -in calc_fcc_ver2.in.lmp -var latconst {i:0.02f} -log log_{j:03d}.lammps'
    x.append(round(i,3))
    file = f"log_{j:03d}.lammps"
    j += 1
    print(command_line)
    args = shlex.split(command_line)
    # p = subprocess.call(args) # Sucess, but much slower...
    p = subprocess.Popen(args) # Sucess!
    p.wait()
    with open(file) as f:
        for line in f:
            if target in line and "print" not in line:
                exec(line.replace("%% ","").replace(";",""))
                y.append(ecoh)

print("--- %s seconds ---" % (time.time() - start_time))

import matplotlib.pyplot as plt
from pylab import *
figure()
plot(x,y,'r*-')
xlabel('Lattice constant (Anstrom)')
ylabel('Cohesive Energy (eV)')
title('aluminum cohesive energy evolution')
show()
