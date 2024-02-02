import matplotlib.pyplot as plt

#example of Axes
# fig = plt.figure()
fig, axes = plt.subplots()
axes.plot([1,2,3], [4,5,6])
axes.set_xlabel('Same to Same')
axes.set_ylabel('Same to Same')
plt.grid(True)
#example of axis

fig, ms = plt.subplots()
ms.plot([1,2,3], [4,5,6])
#set labels for each axis 
ms.set_xlabel('X-axis')
ms.set_ylabel('Y-axis')
plt.grid(True)
plt.show()
