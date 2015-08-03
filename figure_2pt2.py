import numpy as np
import matplotlib.pyplot as plt

u1 = np.random.uniform(0,1,1000)
u2 = np.random.uniform(0,1,1000)

x = u1 + u2
plt.hist(x,4)
plt.show() 