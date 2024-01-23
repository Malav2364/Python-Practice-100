import numpy as np

ra1 = np.random.default_rng()
randomInt = ra1.integers(1,11, size=((2,2)))

randomInt, ix_count, ind_count = np.unique(randomInt, return_counts=True, return_index=True)
print(ix_count, "Count of the elements in the array")
print(ind_count, "Index of the random Array")