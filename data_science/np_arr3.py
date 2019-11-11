import numpy as np

np.random.seed(3)

x2=np.random.randint(10, size=(4,5))
print(x2)

x2_sub=x2[:2,::2]
x2_sub[:][:]=0
print(x2_sub)
print(x2)
print('---------------------------------------')
print()

x2=np.random.randint(10, size=(4,5))
print(x2)
x2_cpy=x2[:2,::2].copy()
x2_cpy[:][:]=0
print(x2_cpy)
print(x2)
