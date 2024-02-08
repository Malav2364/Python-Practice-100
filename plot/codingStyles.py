import numpy as np
import matplotlib.pyplot as plt

#OO style (Object-Oriented Style)

x = np.linspace(0, 2, 100)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x,x, label='linear')
ax.plot(x,x**2, label='quadratic')
ax.plot(x,x**3, label='cubic')
ax.set_title("Simple Plot")
ax.set_xlabel("X-Label")
ax.set_ylabel("Y-Label")
plt.legend()

#using OG plyplot style 

plt.figure(figsize=(5, 2.7), layout='constrained') #fig size ment  for the size of the graph 
plt.plot(x, x, label='Linear')
plt.plot(x, x**2, label='Quadratic')
plt.plot(x, x**3, label='Cubic')
plt.title("Pyplot Style")
plt.xlabel('X-LABEL')
plt.ylabel('Y-LABEL')
plt.legend()
plt.show()