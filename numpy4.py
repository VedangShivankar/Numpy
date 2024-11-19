import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

for row in a:
    print(row)
for cell in row:
    print(cell)

for x in np.nditer(a,order='C',flags=['external_loop']):
    print(x)

for z in np.nditer(a, op_flags=['readwrite']):
    z[...]= z*z
    print(a)

a2 = np.arange(3,15,4).reshape(3,1)

for x,y in np.nditer([a,a2]):
    print(x,y)