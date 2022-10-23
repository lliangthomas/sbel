from numpy import genfromtxt
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg') 


data = genfromtxt('cone_path_iros.csv', delimiter='')
# cone_r_x = data[:,0]
# cone_r_y = data[:,1]
cone_l_x = data[:,2]
cone_l_y = data[:,3]

plt.plot(cone_l_x,cone_l_y,'*')
plt.show()