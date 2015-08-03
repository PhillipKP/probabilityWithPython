import numpy as np
import matplotlib.pyplot as plt

delta = 0.001

n = np.arange((-1/delta),((1/delta)+delta),delta);

print(n)

x2 = 0

for i in n:
	x2 = x2 + (1/np.sqrt(2*np.pi))*np.exp(-(1/2)*np.power(i*delta,2))

print(x2)
