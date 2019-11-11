import numpy as np

np.random.seed(0)

x1=np.random.randint(10, size=6)
x2=np.random.randint(10, size=(3,4))
x3=np.random.randint(10, size=(3,4,5))

print("------------------------------------------")
print(x3)
print("------------------------------------------")
print("x3 ndim: ", x3.ndim)
print("x2 shape: ", x3.shape)
print("x3 size: ", x3.size)
print("x3 dtypr: ", x3.dtype)
print("x3 itemsize: ", x3.itemsize, "bytes")
print("x3 nbytes: ", x3.nbytes, "bytes")
print()

print("------------------------------------------")
print(x1)
print("------------------------------------------")
print("x1[0]: ",x1[0])
print("x1[4]: ",x1[4])
x1[0]=16.84756857
print("x1[0]=16.84756857:", end=' ')
print(x1)
print()


