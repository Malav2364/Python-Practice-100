import numpy as np

a = np.arange(1,11)
np.save('arays10', a) #this will save the numpy file 

#to load the numpy file again and edit it follow the steps 
b = np.load('arays10.npy')
print(b)

#to save the numpy file in other formats like CSV or TXT then follow this steps 

csv_Arr = np.arange(1,15)
np.savetxt('aray10.csv', csv_Arr)

#use loadtxt to load the csv or txt file 
c = np.loadtxt('aray10.csv')
print(c)
