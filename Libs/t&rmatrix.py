import numpy as np

ra1 = np.random.default_rng()
randomArray = ra1.integers(1,11, size=((4,2)))
# print(randomArray)

#here we reshaped an array from its intiaial shape to new shape that is 2,4
reshaped = randomArray.reshape(2,4)
print(reshaped)

#to transpose an array to its original form
#meaning to return the same array size as specified
re = np.arange(15).reshape(5,3)
rs = re.reshape(3,5)
re.transpose()
# print(re)
#alternative 
# print(re.T)

#Reverse an array use flip in numpy
#take an array 
rev = np.arange(1,11).reshape(2,5)
print(rev, "Idhar se udhar")
#to get reverse 
print(np.flip(rev), "Udhar se Idhar")
#array reversed 
#Only rows
print(np.flip(rev, axis=0))#reversed the rows
#Only Columns
print(np.flip(rev, axis=1))#reversed the columns
