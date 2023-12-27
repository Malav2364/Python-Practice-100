from os import sep
from pickletools import float8
import string
import numpy as np


#to create array full with zeros
zero = np.zeros(2)
# print(zero)

#to create array full with Ones
one = np.ones(4)
# print(one)

empt = np.empty(3,np.int16,'F')#here it means that create a empty array with no. of elements passed 
                            #size  datatype
# print("This is empty array with 2 size",empt)

arr = np.arange(11)   #we can create arrays by giving them range for the elements 
# print(arr)

#slicing the arrange arrays 
ar = np.arange(0,101,75)  #here we can give the range from between elements and we can give jump indexes as the last parameter to define 
# print(ar)

ls = np.linspace(0,100,num=10,endpoint=False,retstep=False,dtype=np.int64)    #first the range and  then the gap between the numbers in the arrays 
# ls = np.linspace(0,100,num=10,endpoint=True) this will show the endpoint means the last point of the array 
print(type(ls))