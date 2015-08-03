import numpy as np
import matplotlib.pyplot as plt

u1 = np.random.uniform(0,1,1000)
u2 = np.random.uniform(0,1,1000)
u3 = np.random.uniform(0,1,1000)
u4 = np.random.uniform(0,1,1000)

x = u1 + u2 + u3 + u4
plt.hist(x,7)
plt.xlabel('Smarts')
plt.ylabel('Number of outcomes')
plt.show() 
