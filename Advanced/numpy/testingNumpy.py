import numpy as np

a = np.ones((5,5))

a[1:-1, 1:-1] = np.zeros((3,3))
a[2, 2] = 9

print(a[-1,-1])
