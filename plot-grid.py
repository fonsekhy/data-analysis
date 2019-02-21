#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from test import *

fig, axs = plt.subplots(4,2)

data_arr = []

for i in range(8):
    j = i+1
    data = np.genfromtxt("/path-to-data")
    data_arr.append(data)

for i, each_data in enumerate(data_arr):
    dist  = each_data[:,1]
    force = each_data[:,3]
    a = i/2
    b = i%2
    axs[a,b].plot(dist, force)
    axs[a,b].set_ylabel('Force (pN)', {'color': 'black', 'fontsize':12})
    axs[a,b].set_xlabel('Extention ($\AA$)', {'color': 'black', 'fontsize':12})

plt.savefig('force.svg', format='svg', dpi=300, bbox_inches='tight')
plt.show()
