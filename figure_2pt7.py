import numpy as np
import matplotlib.pyplot as plt

# Number of trials
M = 100000

# The resolution at which we bin the bar plot
delta = 0.0625

x = np.random.normal(0,1,M)

bincenters = np.arange(-3.5, 3.5, delta)
# The length of bincenters
bins = bincenters.size

h = np.zeros(bins)

for i in range(1,M+1):

	for k in range(1,bins+1):

		if (x[i-1] > bincenters[k-1] - delta/2) and (x[i-1] <= bincenters[k-1] + delta/2):
			h[k-1] = h[k-1] + 1


# The histogram divided by the number of trials give you the probability
probest = np.divide(h,M)
# The probability divided by the resolution gives you the PDF
pxest = probest/delta

# THe continue form of the normal pdf
xaxis = np.arange(-4.0,4.0,0.01)
px = (1/np.sqrt(2*np.pi))*np.exp(-0.5*np.multiply(xaxis,xaxis))

plt.plot(bincenters,pxest)
plt.plot(xaxis,px)
plt.show()
