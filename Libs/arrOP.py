import numpy as np


#addition of arrays 
data = np.array([1,2])
ones = np.ones(2, dtype=int)
# print(data + ones)

#subtraction of arrays 
data1 = np.array([1,2])
ones1 = np.ones(2, dtype=int)
# print(data1 * ones1)

#divison of arrays ifp
data2 = np.array([1,2])
ones2 = np.ones(2, dtype=int)
# print(data2 / ones2)

#subtraction of the arrays
data3 = np.array([1,2])
ones3 = np.ones(2, dtype=int)
# print(data2 - ones2)

#addition of the elements in a 1D array
ar1 = np.array([1,2,3,4,5,6,7,8,9])
sm = ar1.sum()
print(sm)

#addition of the elements in a 2D array
ar2 = np.array([[1,1], [2,2]])
sm1 = ar2.sum(axis=0) #use axis 0 for sum of rows
sm2 = ar2.sum(axis=1)#use axis 1 for sum of columns
print(sm1)
print(sm2)