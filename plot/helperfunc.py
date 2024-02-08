import matplotlib.pyplot as plt
import numpy as np


#make a function for plotting same same data on different axes 
def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))

my_plotter(ax1, data1, data2, {'marker' : 'x'})
my_plotter(ax2, data3, data4, {'marker' : 'o'})


#here we understand about styles
fig, ax = plt.subplots(figsize=(5, 2.7))
b = np.arange(len(data1))
ax.plot(b, np.cumsum(data1), color='blue', linewidth=4, linestyle='dotted')
l, = ax.plot(b, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':')
plt.show()
