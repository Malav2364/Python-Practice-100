#import the library for pyplot in matplotlib

import  matplotlib.pyplot as plt

# plt.plot([1,2,3,4]) #to plot the following in the graph

#to give the label to the graph we use label 
plt.ylabel('Some numbers')
plt.xlabel('Some number')

#for multidimensional array 

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.plot([1,2,3,4], [1,4,9,16], 'g^')


#style formatting 
plt.axis((0,6,0,20))
plt.show()

