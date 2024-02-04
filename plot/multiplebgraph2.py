import matplotlib.pyplot as plt
import numpy as np

x = ['Malav', 'Ayush', 'Mayur']
y = [50, 80, 100]
z = [65, 70, 90]
a = [80, 70, 80]

#for multiple showcase of graphs use index of the axis using numpy

p =np.arange(len(x))
#take width as a variable 
width = 0.1

#take width using for loop 
p1 = [j+width for j in p]
p2 = [j+width for j in p1]

plt.bar(p,y, width, color='red',  label='DE')
plt.bar(p1,z, width, color='yellow', label='Maths')
plt.bar(p2,a, width, color='orange', label='DSA')
plt.xlabel('Name', fontsize=15)
plt.ylabel('Marks', fontsize=15)
plt.title('Topper Students')
plt.grid(True)
plt.legend()
plt.xticks(p+width,x)
plt.show()
# print(p1)
