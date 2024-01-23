#first generate a random number 
import numpy as np


rArray = np.random.default_rng()
r_Array = rArray.integers(1,11, size=(10))
# print(r_Array)

a = np.array([2,4,5,7,8,5,9,4])
print(a)
uqval = np.unique(a) #get all unique values form the  arrays 
print(uqval)

uqval, indices_values = np.unique(a, return_index=True)
#this prints the index of the unique values  
print(indices_values)

#practice the code again hahaha

#create a unique array 
uq2 = np.array([2,4,6,5,9,8,7,7])
uv2 = np.unique(uq2)#unique values are here
# print(uv2)

uq2,ui = np.unique(uq2, return_index=True)
# print(ui)
uv2, uc = np.unique(uq2, return_counts=True) #occurence count
# print(uc)
uv2, uinv = np.unique(uq2, return_inverse=True)
# print(uinv)
uAgen = np.random.default_rng()
uqGenAr = uAgen.integers(1,11, size=(4,4))
print(uqGenAr)
uqRows = np.unique(uqGenAr, axis=1)
print(uqGenAr)
#to get them all write them in a same syntax and task will be done 

