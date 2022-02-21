import numpy as np
a = np.array([1,2,3,4,5])
print(a)
print(a.shape)# Analyze the array
print(a.dtype)# Checking data type
print(a.ndim)# bumber of dimenaions
print(a.size)# Total nber of elements
print(a.itemsize)# Size in bytes of each element
print(a[0])
a[3]=23# Assigning and changing value of elements in a list
print(a)

b = a* np.array([2,0,2,3,4])
print(b)