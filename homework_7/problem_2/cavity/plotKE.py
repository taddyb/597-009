#!/usr/bin/env python
import os, sys
import math
from numpy import loadtxt
import matplotlib.pyplot as plt

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel("KE", fontsize=16); 
plt.xlabel("time (s)", fontsize=16); 
plt.title("KE over time", fontsize=16)
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

fileName = "/home/tbindas/OpenFOAM/tbindas-8/homework_7/problem_2/cavity/logs/Separator_0"
time = []
ke = []
abc =loadtxt(fileName, skiprows=0)
for z in abc:
	time.append(z[0])
	ke.append(z[1])

plt.plot(time,ke,'k',label="$ke$")

plt.legend(loc='upper left')

plt.savefig("plotke_python.png")
#plt.show()

print("Done!")
