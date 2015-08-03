import numpy as np
import matplotlib.pyplot as plt

# Number of noise trials
M = 1000

# The range of values of A (amplitude)
A = np.arange(0.1,5.1,0.1)
Pe = np.zeros(A.size)
for k in range(1,A.size+1):
	error = 0
	for i in range(1,M+1):
		w = np.random.normal(0,1,1)
		if A[k-1]/2 + w <= 0:
			error = error + 1

	Pe[k-1] = error/M

plt.plot(A,Pe);
plt.show()
