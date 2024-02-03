import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.1, 4, 0.2)
# print(a)

#plotting the points on the graph
plt.plot(a, a, 'r--', a,a**2,'bs', a, a**3, 'g^' )
plt.show()
