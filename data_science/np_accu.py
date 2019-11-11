import numpy as np
from scipy import special

L= np.random.random(1000000)
print(np.sum(L))

print(np.min(L))
print(np.max(L))
print('-----------------------------------------')

M=np.random.random((3,4))
print(M)
print(M.sum())
print(M.min())
print(M.min(axis=0))
print(M.min(axis=1))


