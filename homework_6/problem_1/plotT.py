#!/usr/bin/env python
import os, sys
import math
from numpy import loadtxt
import matplotlib.pyplot as plt

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel(" T (degree)", fontsize=16); 
plt.xlabel(" Distance along Diagonal ", fontsize=16); 
plt.title(" $T$ at probe point ", fontsize=16)
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

#plot T
fileName = "{}/postProcessing/probes/0/T"
files_list = [
"10x10",
"50x50",
"100x100"
]
T=[]
distance=[
0.075,
0.22499999999999998,
0.37499999999999994,
0.5249999999999999,
0.6749999999999998,
0.8249999999999997,
0.9749999999999998,
1.1249999999999998,
1.2749999999999997,
1.4249999999999996
]
for f in files_list:
    abc =loadtxt(fileName.format(f), skiprows=0)
    for z in abc:
	T.append(z[1])
    plt.plot(distance,T,'k',label=f)

plt.legend(loc='upper left')
plt.savefig("plotT_problem1.png")
#plt.show()

print("Done!")
