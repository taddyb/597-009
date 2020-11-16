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

#plot U
#Taken from postProcessing/probes/0/U time 2
Ux = [0.974995,0.874974,0.774956,0.674943,0.574935,0.474933,0.374938,0.274949,0.174965,0.0749843 ,0.0249947]
Uy = [0,0,0,0,0,0,0,0,0,0 ,0]
fileName = "postProcessing/probes/0/U"
distance = np.arange(0,1, 0.0999).tolist()
distance.reverse()
plt.plot(distance,Ux,'k',c="red", label="U(x)")
plt.plot(distance,Uy,'k',c="blue", label="U(y)")
plt.legend(loc='upper right')
plt.savefig("plotUx.png")

#plt.show()

print("Done!")
