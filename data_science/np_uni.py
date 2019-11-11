#Loop is slow

import numpy as np

np.random.seed(4)

def reci(n):
    output=np.empty(len(n))
    for i in range(len(n)):
        output[i]=1.0/n[i]
    return output

a=np.random.randint(1,100,size=500000)
print(reci(a))
print(1.0/a)

