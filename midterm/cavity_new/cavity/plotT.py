#!/usr/bin/env python
import os, sys
import math
import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel(" U ", fontsize=16); 
plt.xlabel(" Distance from the x-axis", fontsize=16); 
plt.title(" U along center line", fontsize=16)
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

#plot T
fileName = "postProcessing/probes/0/U"
distance = np.arange(0,1, 0.0999).tolist()
txt = loadtxt(fileName, skiprows=0)
print(txt)
plt.plot(distance,txt[1][1:],'k',label=f[0], c=f[1])

plt.legend(loc='upper right')
plt.savefig("plotT_problem1.png")
#plt.show()

print("Done!")
