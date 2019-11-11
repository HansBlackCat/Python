import numpy as np

theta=np.linspace(0, np.pi, 3)
print('------------------------------------------')

print("theta      = ",theta)
print("sin(theta) = ",np.sin(theta))
print("cos(theta) = ",np.cos(theta))
print("acos(theta)= ",np.arccos(theta))
print("sec(theta) = ",1.0/np.cos(theta))
print('------------------------------------------')

x=[1,2,3]
print("x    = ",x)
print("e^x  = ",np.exp(x))
print("3^x  = ",np.power(3,x))
print("lnx  = ",np.log(x))
print("logx = ",np.log10(x))
print('------------------------------------------')

y=np.array([1/pow(10,i) for i in range(5)])
print("exp(x)-1 = ",np.expm1(x))
print("log(1+x) = ",np.log1p(x))

