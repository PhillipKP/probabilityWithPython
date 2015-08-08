import numpy as np
import matplotlib.pyplot as plt

M = 100000
X = np.random.normal(0,1,M);
Y = np.random.normal(0,1,M);

d = np.sqrt(np.square(X) + np.square(Y))

avgd = np.mean(d);

print(avgd)
