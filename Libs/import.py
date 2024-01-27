import numpy as np
import pandas as pd

# x = pd.read_csv('aray10.csv', header=1).values
# print(x)

a = np.arange(1,11)
# print(a)

#use np.save to save the file 
np.save('animal', a)
#load the npy file 
b = np.load('animal.npy')
# print(b)

#to save in csv 
np.savetxt('aray.csv', b)
d = np.loadtxt('aray.csv')
# print(d)

#to print the csv file using pandas

x = pd.read_csv('aray.csv', header=0).values
print(x)