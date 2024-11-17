import numpy as np
n = [6,7,8]
print(n[0:2])
print(n[-1])

a = np.array([[6,7,8], [1,2,3], [9,3,2]])
print(a)
print(a[1,2])
print(a[0:2,2])
print(a[-1])
print(a[-1:0,2])
print(a[:,1:3])

b = np.array([[6,7,8], [1,2,3], [9,3,2]])
print(b)
for cell in b.flat:
    print(cell)
b = np.arange(6,12).reshape(3,2)
a = np.arange(6).reshape(3,2)
np.vstack((a,b))
np.hstack((a,b))
b = np.arange(20).reshape(4,13)
np.hsplit(b,3)