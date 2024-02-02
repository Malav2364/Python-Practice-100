import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

#create a figure using single axis 
# fig, ax = plt.subplots()
# ax.plot([1,2,3,4], [1,4,2,3])
# plt.show()

#create a empty figure 

fig = plt.figure()
fig, ax = plt.subplots() #a figure with single axes
fig, axs = plt.subplots(2,2) #a figure with 2X2 grid axes
fig, axss = plt.subplots(4,4) #a figure with 4X4 grid axes
#a figure with one axis on left and two axis on right
fig, axss = plt.subplot_mosaic([['left', 'right_top',], ['left', 'right_bottom']]) 
plt.show()


#AXIS means specific x-axis or y-axis 
#AXES means plural of AXIS that refers to the whole plotting area 