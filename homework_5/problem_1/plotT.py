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

T=[141.667, 202.778, 241.667, 258.333, 252.778, 225]
distance=[0.0, 0.0033, 0.0066, 0.0099, 0.013, 0.016]

plt.plot(distance,T,'k',label="Plot of T vs distance")

plt.legend(loc='upper left')

plt.savefig("plotT_python.png")
#plt.show()

print("Done!")
