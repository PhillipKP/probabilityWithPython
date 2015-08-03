import numpy as np
import matplotlib.pyplot as plt

# Trials
M = 10000

temp1 = np.random.uniform(0,1,M);
bool1 = temp1 > .5
# convert boolean arrays to interger arrays 
x1 = bool1.astype(int)

temp2 = np.random.uniform(0,1,M);
bool2 = temp2 > 0.5
x2 = bool2.astype(int)

print(x1)
print(x2)
t = np.multiply(x1,x2)
t1 = (t == 0).sum()
t2 = (t == 1).sum()
print(t)
print(t1)
print(t2)
relFreqZeros = t1/M
relFreqOnes = t2/M

print('The relative frequency of 0\'s is {} '.format(relFreqZeros))
print('The relative frequency of 1\'s is {} '.format(relFreqOnes))
print('The sum of the relative frequencies is {}'.format(relFreqZeros + relFreqOnes))


