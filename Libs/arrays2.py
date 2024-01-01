'''This is a vertical stack of the array'''

import numpy as np

ar1 = np.array([1,2,3,4,5,6,7,8,9,10])

#here we sliced array from 3 to 8 index and printed
ar2 = ar1[3:8]
# print(ar1) #original
# print(ar2)#sliced

ar3 = np.array([[2,3,6,4], 
                        [1,5,7,9]])
ar4 = np.array([[2,3,6,4], 
                        [1,5,7,9]])

c = np.vstack((ar3, ar4)) #stack both array in horizontal manner
# print("Horizontal :",c)

d = np.hstack((ar3, ar4))#stack both array in vertical manner 
# print("Vertical :",d)

#reshaping the arange array directly 
e = np.arange(1,25).reshape(2,12)
# print(e)

#splitting the array in equal parts
f = np.hsplit(e, 3)
# print(f)

#splitting the array from specific index

g = np.hsplit(e,(3,4))
# print(g)

k = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
m = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(k)

#stacking the arrays horizontally and vertically using vsplit and hsplit
l = np.vstack((k,m))
# print(__doc__,l)
n = np.hstack((k,m))
# print(n)

#create and reshape the array at same time
ms = np.arange(1,25).reshape(2,12)
# print("This is an array directly reshaped when created")
# print(ms)

#now if we want to split the array in to hsplit or vslpit wecan do this 

aa = np.hsplit(ms, 2)
# print(aa)

mm = np.vsplit(ms, 2)
# print(mm)

#crete an array and slice it and modify the first element of the array 
ca = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
#slicing
b1 = ca[0, :]
# print(b1)
b1[0] = 100
print(ca)

#copying the array 
b2 = ca.copy()
print(b2)