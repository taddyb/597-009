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
plt.title(" Ux and Uy un-normalized for cavity", fontsize=16)
plt.yscale("log")
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

files_list_norm = [
["logs/normFactor_0","red", "U(x)"],
["logs/normFactor_1","blue", "U(y)"],
]
files_list_residual = [
["logs/Ux_0","red", "U(x)"],
["logs/Uy_0","blue", "U(y)"],
]
U=[]
for i in range(len(files_list_norm)):
    txt_norm = loadtxt(files_list_norm[i][0], skiprows=0)
    txt_x_norm = [x.tolist()[0] for x in txt_norm]
    txt_y = [x.tolist()[1] for x in txt_norm]
    txt_residual = loadtxt(files_list_residual[i][0], skiprows=0)
    txt_x_residual = [x.tolist()[0] for x in txt_residual]
    x_un_normal = [txt_x_norm[i] * txt_x_residual[i] for i in range(len(txt_x_norm))] 
    plt.plot(x_un_normal, txt_y,'k',label=files_list_norm[i][2], c=files_list_norm[i][1])

plt.legend(loc='upper right')
plt.savefig("plotUnNormal.png")
#plt.show()

print("Done!")
