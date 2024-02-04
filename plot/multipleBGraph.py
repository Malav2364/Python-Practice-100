import matplotlib.pyplot as plt
import numpy as np

#example of  bar graph with 
x = ['Python', 'C', 'C++', 'Java', 'JS', 'Rust']
y = [100, 90, 85, 90, 89, 60]
z = [50, 60, 20, 80, 60, 90]
p = np.arange(len(x))
width = 0.2
p1 = [j+width for j in p]
plt.title('Language Popularity from 100')
plt.xlabel('Languages', fontsize=15)
plt.ylabel('Popularity', fontsize=15)
plt.bar(p,y, width, color="orange", label='Popularity', align='edge') #width is used to give width to the bars in the  graph  and align for the alignment of the bars on the labels in x axis
plt.grid(False)
plt.minorticks_on()
#multiple bar graphs in a single axes
plt.bar(p1,z, width, color="yellow", label='Popularity2', align='edge')
plt.legend()
plt.xticks(p+width, x)

# plt.legend(x,y)
# plt.show()
print(p)