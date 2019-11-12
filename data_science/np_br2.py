#!usr/bin/env python3
import numpy as np

X=np.random.random((10,3))
print(X)

Xmean=X.mean(0)
print(Xmean)

X_centered=X-Xmean 
print(X_centered.mean(0))
