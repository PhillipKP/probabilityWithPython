import numpy as np
import matplotlib.pyplot as plt

noiseTrials = 600000

t = np.random.randint(1,7,noiseTrials)
print(t)
hist = np.bincount(t)
print(hist/noiseTrials)

