#!/usr/bin/env python
import os, sys
import math
from numpy import loadtxt
import matplotlib.pyplot as plt

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel(" T (degree)", fontsize=16); 
plt.xlabel("Distance", fontsize=16); 
plt.title(" $T$ over the total distance", fontsize=16)
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

T=[1.00083, 1.00661, 1.04132, 1.24959, 2.49917]
distance=[0.1, 0.3, 0.5, 0.7, 0.9]

plt.plot(distance,T,'k',label="Plot of T vs distance")

plt.legend(loc='upper left')

plt.savefig("plotT_python.png")
#plt.show()

print("Done!")
