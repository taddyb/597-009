#!/usr/bin/env python
import os, sys
import math
import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel("U (log scale)", fontsize=16); 
plt.xlabel("Time", fontsize=16); 
plt.title(" Ux and Uy rediduals for cavity_new", fontsize=16)
plt.yscale("log")
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

files_list = [
["logs/Ux_0","red", "U(x)"],
["logs/Uy_0","blue", "U(y)"],
]
U=[]
for f in files_list:
    txt = loadtxt(f[0], skiprows=0)
    txt_x = [x.tolist()[0] for x in txt]
    txt_y = [x.tolist()[1] for x in txt]
    plt.plot(txt_x, txt_y,'k',label=f[2], c=f[1])

plt.legend(loc='upper right')
plt.savefig("plotResiduals.png")
#plt.show()

print("Done!")
