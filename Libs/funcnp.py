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
# print(type(ls))

pc = np.array([1,2,3,4,5,6,7,8])
# print(pc)


#Adding Removing and Sorting Elements
#concatination of Arrays

pr = np.arange(6)
# print("This is Array 1 :",pr)

pa = np.arange(6)
# print("This is Array 2 :",pa)

cc = np.concatenate((pr, pa))
# print(cc)

#Concatenate type 2 
x = np.array([[5, 3], [7, 6]])
y = np.array([[8, 9]])

z = np.concatenate((x,y), axis=0)
# print(z)

#some sorting methods

a = np.array([5, 6, 7, 8])
b = np.array([1, 2, 3, 4])
# c = np.concatenate((a,b))
# print(c)
# d = np.sort(c)
# print("Sorted Array :",d)
# print(d.searchsorted(2)) #to search in sorted arrays

#lex sort 
# names_ages = [('Alice', 25), ('Bob', 30), ('Carol', 28)]
# indices = np.lexsort([name, ages])
# for i in indices:
#     print(names_ages[i]) 

#SHAPE SIZE OF ARRAY

td = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

#determine the shape of the array
# print(td.shape)

#determine the size of the array
# print(td.size)

#determine the dimension of array
# print(td.ndim)

#reshaping the array
f = np.arange(6)
g = f.reshape(2,3)     #columns and rows
# print(g)

#reshaping part 2
h = np.reshape(f, newshape=(2,3), order='C')
# print(h)

#adding axis to arrays or converting of 1d array to 2d array 
i = np.arange(6)
j = i[np.newaxis,:]   #added a row in the array 
# print(j.shape)

k = i[:, np.newaxis]
# print(k.shape)          #added a column in the array 

# to add row or column at a particular axis 
b = np.expand_dims(f, axis=0)  #add row
# print(b.shape)
v = np.expand_dims(f, axis=1) #add column
# print(v.shape)

#indexing and slising 
#just take an array 

#indexing of the array same as in list or tuple
#index finder 
array1 = np.arange(1)
# print(array1[1]) #this prints the index of the element present in array 
for i in range(array1.size):
    print(f"index of  [{array1[i]}] :",i)

#other types of indexing in python 
array2 = np.arange(5)
print(array2[1:]) #from index 1 till last element 
print(array2[:3]) #from staring till index 3 
print(array2[-2:]) #means last 2 elements from the array 
print(array2[1:4]) #for specific array indexing