#!/usr/bin/env python
import os, sys
import math
import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel(" T (degree)", fontsize=16); 
plt.xlabel(" Distance along Diagonal ", fontsize=16); 
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

#plot T
fileName = "{}/postProcessing/probes/0/T"
files_list = [
["10x10","red"],
["50x50","blue"],
["100x100","black"]
]
T=[]
distance = np.arange(0,1.411, 0.141).tolist()

for f in files_list:
    txt = loadtxt(fileName.format(f[0]), skiprows=0)
    plt.plot(distance,txt[1][1:],'k',label=f[0], c=f[1])
    plt.title(" $T$ along diagonal at time 0s ", fontsize=16)
    plt.legend(loc='upper right')
    plt.savefig("plotT_problem2_0s.png")

plt.clf()
plt.figure(1);
plt.ylabel(" T (degree)", fontsize=16); 
plt.xlabel(" Distance along Diagonal ", fontsize=16); 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()
    
for f in files_list:
    txt = loadtxt(fileName.format(f[0]), skiprows=0)
    plt.plot(distance,txt[1000][1:],'k',label=f[0], c=f[1])
    plt.title(" $T$ along diagonal at time 1s ", fontsize=16)
    plt.legend(loc='upper right')
    plt.savefig("plotT_problem2_1s.png")


#plt.show()

print("Done!")
