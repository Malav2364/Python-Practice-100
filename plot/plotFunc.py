import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

data = {
    'a' : np.arange(50),
    'c' : np.random.randint(0,50,50),
    'd' : np.random.randn(50) * 100
}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
#creating a scatter plot 

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained', linewidth=0.1)
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')

plt.grid(False)
plt.show()


