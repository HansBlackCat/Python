#!/usr/bin/env python3

import numpy as np

a=np.array([0,1,2])
b=np.array([5,5,5])
print(a+b)

M=np.ones((3,3))
print(M+a)
print('-----------------------------------')

a=np.arange(3)
b=np.arange(3)[:,np.newaxis]
print(a)
print(b)
print(a+b)
print('-----------------------------------')

M=np.ones((2,3))
a=np.arange(3)
print(M+a)
print('-----------------------------------')

M=np.arange(6).reshape((3,2))
a=np.arange(3)
arr=np.logaddexp(M,a[:,np.newaxis])
print(arr)


