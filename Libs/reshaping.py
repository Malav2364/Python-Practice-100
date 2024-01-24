import numpy as np

ar1 = np.array([[1,2], [3,4], [5,6], [7,8]])
#here the array is in multidimensional form 2,4 size
#here we want to faltten this array and store in another variable
print(ar1, "Before flattening")
ar2 = ar1.flatten()
print(ar2, "After flattening")
#but this will not change main shaping of the array

#to change main shaping and save in new array  we need to use ravel function in NP
ar3 = np.array([[1,2],[3,4],[5,6]])
# print(ar3)
ar4 = ar3.ravel()
print(ar4)#here we got a new array
#try to access the new array
print(ar4[0]) #here new array is stored and accessed 