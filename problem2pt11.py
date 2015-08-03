import numpy as np
import matplotlib.pyplot as plt

# This script is for the Intuitive Probability and Random Processes using MATLAB 
# but I'm really using Python with numpy and matplotlib
#
# This is for problem 2.11

M = 10000
U = np.random.uniform(0,1,M)
X = 2*U
mu = np.mean(X)

print(mu)

