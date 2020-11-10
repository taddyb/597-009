#!/usr/bin/env python
import os, sys
import math
from numpy import loadtxt
import matplotlib.pyplot as plt

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel(" T (degree)", fontsize=16); 
plt.xlabel(" Time (s) ", fontsize=16); 
plt.title(" $T$ at probe point ", fontsize=16)
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

#plot T
fileName = "postProcessing/probes/0/T"
T=[]
time=[]
abc =loadtxt(fileName, skiprows=0)
for z in abc:
	time.append(z[0])
	T.append(z[1])

plt.plot(time,T,'k',label="probe 1")

plt.legend(loc='upper left')

plt.savefig("plotT_python.png")
#plt.show()

print("Done!")
