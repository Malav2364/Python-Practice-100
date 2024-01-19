#2d arrays are also calles matrices

#creating a matrice or 2d array

import numpy as np

data = np.array([[1,2], [3,4], [5,6]])
print(data)

#slicing operations
print(data[0,1]) #0th index of row and 1st index of column

print(data[0:1])# : means from any index to any index if only one index is given then from that index to last row will be printed

print(data[:2]) #vice versa of above given logic

print(data[0:2 , 0]) #from 2nd element in the column to 0th element in the row


#min max functions 

print(data.max() ,data.sum(), data.min())

#min max in axis in matrix
print(data)
print(data.max(axis=0)) #prints the highest value in columns
print(data.max(axis=1)) #prints the highest value in rows

#addition of two matrix

data1 = np.array([[1,2], [3,4]])
data2 = np.array([[1,1], [1,1]])    #only add if they have same height means same rows and columns
print(data1 + data2)

#non same height will led to broadcasting for all rows and columns

data3 = np.array([[1,2], [3,4], [5,6]])
data4 = np.array([[1,1]])   #this will add 1,1 to all the rows is called broadcasting
print(data3+data4)