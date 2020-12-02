#100           (0.877332 -0.0922299 -0.0530688) (0.877332 -0.0922299 -0.0530688) (-0.0979042 -0.637776 0.0173383) (-0.00490345 -0.226045 -0.070638) (0.322381 -0.483158 0.187066) (0.108499 0.756732 0.0680508) (0.0470846 0.526538 0.13271) (0.285643 0.682775 -0.0492823) (0.387648 0.218713 -0.252178) (0.780835 -0.719312 -0.05275) (0.60959 -0.488715 0.0614446) (0.60959 -0.488715 0.0614446) (0.638294 -0.483912 0.0640366) (0.87616 -0.0197952 0.0835386) (1.07143 0.403029 0.0304551) (1.14214 0.358865 -0.120868) (1.19461 0.545854 -0.0863591) (1.0831 0.294636 0.0282866)


# Probe 0 (-1 0 0)
# Probe 1 (-0.75 0 0)
# Probe 2 (-0.5 0 0)
# Probe 3 (0.5 0 0)
# Probe 4 (0.75 0 0)
# Probe 5 (1 0 0)
# Probe 6 (1.25 0 0)
# Probe 7 (1.5 0 0)
# Probe 8 (1.75 0 0)
# Probe 9 (2 0 0)
# Probe 10 (2.25 0 0)
# Probe 11 (2.5 0 0)
# Probe 12 (2.75 0 0)
# Probe 13 (3 0 0)
# Probe 14 (3.25 0 0)
# Probe 15 (3.5 0 0)
# Probe 16 (3.75 0 0)
# Probe 17 (4 0 0)

#!/usr/bin/env python
import os, sys
import math
from numpy import loadtxt
import numpy as np
import matplotlib.pyplot as plt

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel("U", fontsize=16); 
plt.xlabel("X coordinate", fontsize=16); 
plt.title("U contour at time 100", fontsize=16)
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])
X = [-1, -0.75, -0.5, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4]
Ux = []
Uy = []
Uz = []
u_100 = [(0.877332, -0.0922299, -0.0530688), (0.877332, -0.0922299, -0.0530688), (-0.0979042, -0.637776, 0.0173383), (-0.00490345, -0.226045, -0.070638), (0.322381, -0.483158, 0.187066), (0.108499, 0.756732, 0.0680508), (0.0470846, 0.526538, 0.13271), (0.285643, 0.682775, -0.0492823), (0.387648, 0.218713, -0.252178), (0.780835, -0.719312, -0.05275), (0.60959, -0.488715, 0.0614446), (0.60959, -0.488715, 0.0614446), (0.638294, -0.483912, 0.0640366), (0.87616, -0.0197952, 0.0835386), (1.07143, 0.403029, 0.0304551), (1.14214, 0.358865, -0.120868), (1.19461, 0.545854, -0.0863591), (1.0831, 0.294636, 0.0282866)]
for probe in u_100:
    Ux.append(probe[0])
    Uy.append(probe[1])
    Uz.append(probe[2])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

# fileName = "/home/tbindas/OpenFOAM/tbindas-8/homework_7/problem_2/cavity/logs/Separator_0"
# time = []
# ke = []
# abc =loadtxt(fileName, skiprows=0)
# for z in abc:
# 	time.append(z[0])
# 	ke.append(z[1])

plt.plot(X,Ux,'k',label="$Ux$", color="b")
plt.plot(X,Uy,'k',label="$Uy$", color="r")
plt.plot(X,Uz,'k',label="$Uz$", color="orange")


plt.legend(loc='upper left')

plt.savefig("plot_u_python.png")
#plt.show()

print("Done!")
