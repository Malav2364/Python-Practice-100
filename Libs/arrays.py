import numpy as np

#array slicing 
ar1 = np.array([[1,2,3], [4,5,6], [7,8,9],[10,11,12]])
# print(ar1[ar1 > 5]) #here we printed elements greater than 5 

#greater than equal to 5 prints
# print(ar1[ar1 != 5])
# print(ar1[ar1 < 5])
# print(ar1[ar1 >= 5])
# print(ar1[ar1 <= 5])
# print(ar1[ar1 == 4 & ar1 == 8]) not possible 

#to print divisible by any number

# print("Elements Divisible by 2 :",ar1[ar1%2 == 0],)
# print("Elements Divisible by 3 :",ar1[ar1%3 == 0])
# print("Elements Divisible by 6 :",ar1[ar1%6 == 0])
# print("Elements Divisible by 4 :",ar1[ar1%4 == 0])

#for using operations 
# print(ar1[(ar1 > 5) & (ar1< 10)]) #AND operator 
# print(ar1[(ar1 > 5) | (ar1< 3)])    #OR operator

#for direct array elements entering in the array 
fip = (ar1 < 5) | (ar1 == 10) # so we stored it in a variable and got an outut as boolean like TRUE or FALSE
# print(fip)

#using the non zero function
b = np.array([[12,32,21],[56,65,89], [21,56,47]])
c = np.nonzero(b < 40)
print(c)
