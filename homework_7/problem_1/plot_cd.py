

#!/usr/bin/env python
import os, sys
import math
from numpy import loadtxt
import numpy as np
import matplotlib.pyplot as plt

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel("Cd", fontsize=16); 
plt.xlabel("Case number", fontsize=16); 
plt.title("Cd per case", fontsize=16)
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])
cases=[1,2,3]
cd=[0.4725943e-01, 6.270459e-01, 3.501515e-01]
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

plt.plot(cases, cd,'k',label="$Cd$")


plt.legend(loc='upper left')

plt.savefig("plot_cd.png")
#plt.show()

print("Done!")
