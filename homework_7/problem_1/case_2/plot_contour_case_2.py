#!/usr/bin/env python
import os, sys
import math
from numpy import loadtxt
import numpy as np
import matplotlib.pyplot as plt

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(1);
plt.ylabel("U", fontsize=16); 
plt.xlabel("X coordinate", fontsize=16); 
plt.title("U contour at time 100", fontsize=16)
#plt.xlim([0,0.16])
#plt.ylim([-0.4,0.4])
X = [-1, -0.75, -0.5, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4]
Ux = []
Uy = []
Uz = []
u_100 = [(0.996896, 0.00235828, -5.72095e-08), (0.799121, 0.0192646, -3.57301e-08), (0.0162205, -0.0510692, -2.3286e-05), (0.000590584, -0.0662067, -1.14321e-06), (-0.173548, -0.244808, -1.5667e-09), (-0.401541, 0.0784425, 1.98692e-07), (-0.458672, 0.369785, 1.73805e-07), (-0.428797, 0.643925, 6.25356e-08), (-0.260455, 0.807386, -2.68925e-07), (-0.0366927, 0.574569, -1.81473e-07), (0.365699, -0.0921899, -1.11686e-07), (0.595893, -0.544904, -7.45811e-08), (0.826997, -0.876937, 2.07938e-08), (0.880656, -0.846073, -1.21884e-08), (0.847668, -0.707882, -7.90948e-08), (0.790581, -0.606028, -1.05402e-08), (0.812234, -0.0253981, -1.85424e-07), (0.859894, 0.464897, -1.98716e-07)]

for probe in u_100:
    Ux.append(probe[0])
    Uy.append(probe[1])
    Uz.append(probe[2])

#change the fontsize of minor ticks label 
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
plt.grid()

# fileName = "/home/tbindas/OpenFOAM/tbindas-8/homework_7/problem_2/cavity/logs/Separator_0"
# time = []
# ke = []
# abc =loadtxt(fileName, skiprows=0)
# for z in abc:
# 	time.append(z[0])
# 	ke.append(z[1])

plt.plot(X,Ux,'k',label="$Ux$", color="b")
plt.plot(X,Uy,'k',label="$Uy$", color="r")
plt.plot(X,Uz,'k',label="$Uz$", color="orange")


plt.legend(loc='upper left')

plt.savefig("plot_u_python.png")
#plt.show()

print("Done!")
