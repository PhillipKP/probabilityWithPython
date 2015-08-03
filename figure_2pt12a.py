import numpy as np
import matplotlib.pyplot as plt

#  Number of Noise Trials
M = 1000
u1 = np.random.uniform(0,1,M)
u2 = np.random.uniform(0,1,M)

x1 = u1
x2 = u2

plt.scatter(x1,x2)
plt.xlim(0,1.5)
plt.ylim(0,1.5)
plt.grid(True)
plt.show()
