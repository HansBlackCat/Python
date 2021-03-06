import numpy as np
import matplotlib.pyplot as plt

a='k'
x=np.linspace(0,5,50)
y=np.linspace(0,5,50)[:,np.newaxis]
z=np.sin(x)**10+np.cos(10+y*x)*np.cos(x)

plt.imshow(z,origin='lower',exten=[0,5,0,5],cmap='viridis')
plt.colorbar();