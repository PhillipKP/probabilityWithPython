import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111)

u1 = np.random.uniform(0,1,8)
u2 = np.random.uniform(0,1,8)
x = u1 + u2
print(x)
numBins = 4
ax.hist(x,numBins,color='green',alpha=0.8)
plt.show()