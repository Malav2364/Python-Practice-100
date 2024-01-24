import numpy as np

ra1 = np.random.default_rng()
randomInt = ra1.integers(1,11, size=((2,2)))

randomInt, ix_count, ind_count, inv_arr = np.unique(randomInt, return_counts=True, return_index=True, return_inverse=True)
print(ix_count, "Count of the elements in the array")
print(ind_count, "Index of the random Array")
print(inv_arr, "Inverse Array Returned")
#practice of random array is done ✅
