#!/usr/bin/env python
import os, sys
import math
from numpy import loadtxt
import matplotlib.pyplot as plt

#Setup the plotting environment
#This assumes you have Latex setup in your system. If not, just 
#comment out this line. Otherwise, Python throws out an error.
#plt.rc('text', usetex=True)  
#This sets the default font to be "serif". 
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel(" Velocity components (m/s)", fontsize=16); 
plt.xlabel(" Distance (m) ", fontsize=16); 
plt.title(" $U_x$ and $U_y$ along diagonal sample line ", fontsize=16)
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

#plot Ux and Uy
fileName = "postProcessing/sample/10/data_U.xy"
Ux=[]
Uy=[]
dist=[]
abc =loadtxt(fileName, skiprows=0)
for z in abc:
	dist.append(z[0])
	Ux.append(z[1])
	Uy.append(z[2])

plt.plot(dist,Ux,'k',label="$U_x$")
plt.plot(dist,Uy,'r--',label="$U_y$")

plt.legend(loc='upper left')

plt.savefig("plotU_python.png")
#plt.show()

print("Done!")
