import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# vertical stack
vstack = np.vstack((a,b))
print(vstack)

# horizontal stack
hstack = np.hstack((a,b))
print(hstack)