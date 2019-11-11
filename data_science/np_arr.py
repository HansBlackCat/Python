import numpy as np

a=np.array([1,4,6])
print(a)
b=np.array([3.14,4,2,3])
print(b)
c=np.array([1,2,3,4], dtype='float32')
print(c)
d=np.array([range(i,i+3) for i in [3,6,9]])
print(d)
print()

e=np.zeros(10, dtype='int')
print(e)
f=np.ones((3,5), dtype='int')
print(f)
g=np.full((2,5), 3.14)
print(g)
h=np.arange(0,10,2)
print(h)
i=np.linspace(0,10,3)
print(i)
print()

j=np.random.random((3,3))
print(j)
k=np.random.normal(50,20,(5,5))
print(k)
l=np.random.randint(0,100,(3,3))
print(l)
m=np.eye(4)
print(m)
n=np.empty(3)
print(n)








