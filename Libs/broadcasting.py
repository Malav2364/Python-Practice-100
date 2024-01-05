#broadcasting
#create an array and convert km into m
#means to perfrom the operation with each element in the array 
import numpy as np

km = np.array([2,3,6,4])
m = km * 1000
print(m)

# for i in km:
#     m = i*1000
#     print(f"{i} Km = {m} m")