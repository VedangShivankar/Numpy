import numpy as np 

a = np.array([5,6,9])
print(a.max)
print(a.min)
print(a.sum)
print(a.sqrt)

b = np.array([[1,2],[3,4],[5,6]])
print(b.ndim)
print(b.itemsize)
print(b.dtype)

c = np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
print(c.itemsize)
print(a.size)
print(c.shape)
print(c.reshape(2,3))