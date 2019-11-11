import numpy as np

np.random.seed(18)

grid=np.arange(0,16).reshape(2,8)
print(grid)
print()

x=np.array([1,2,3])
print(x.reshape(1,3))
print(x.reshape(3,1))
print()

x=np.array([1,2,3])
y=np.array([3,4,5])
print(np.concatenate((x,y)))
z=np.array([9,9,9])
print(np.concatenate((x,y,z)))
print()

x2=np.random.randint(0,10,(2,3))
print(x2)
print(np.concatenate((x2,x2)))
print(np.concatenate((x2,x2),axis=1))
print()

print(np.vstack((x,x2)))


