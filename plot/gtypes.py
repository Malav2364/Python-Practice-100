import matplotlib.pyplot as plt
import numpy as np

#example of  bar graph with 
x = ['Python', 'C', 'C++', 'Java', 'JS', 'Rust']
y = [100, 90, 85, 90, 89, 60]
c = ['y', 'g', 'b', 'black', 'magenta', 'pink']
plt.title('Language Popularity from 100')
plt.xlabel('Languages', fontsize=15)
plt.ylabel('Popularity', fontsize=15)
plt.bar(x,y, width=0.5, color=c, align='center') #width is used to give width to the bars in the  graph  and align for the alignment of the bars on the labels in x axis
plt.grid(False)
plt.minorticks_on()


# plt.legend(x,y)
plt.show()