import numpy as np

#let's start with arrays 
#creation of Arrays
a = np.array([1,2,3,5,6,7,8,9,10])  #single dimension array
print("Single Dimension Array")
print(a)

print(" ")

b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("3D array or Multi dimensional Array")
print(b)

#now array indexing in the multidimensional array

print(b[0]) #for accessing the row in 3d array 
print(b[0,1]) #for accessing the element from a row 