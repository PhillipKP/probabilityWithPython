import numpy as np
import matplotlib.pyplot as plt


M = 10000 
p1 = 0.4
p2 = 1 - p1

x = []
relp = []
x1 = 1 # 1 represents heads
x2 = 0 # 0 represents tails

for i in range(1,M):
    # Generate a random number drawn from a uniform probability
    # distribution between and including 0 and 1.    
    u = np.random.uniform(0,1,1)
    
    if u <= p1:
	# If the random number is less than the probability p1
	# then append a number denoting a heads 
        x.append(x1)
    elif u > p1 and u <= p2:
	# If the random mumber is between p1 and p2 including p2 then
	# append a number denoting a tails
        x.append(x2)

    # the relative probability is equal to the number of heads divided by
    # the total number of trials
    temps = sum(x)/i
    temps = float(temps)
    relp.append(temps)


plt.plot(relp)
plt.xlabel('Number of trials', fontsize = 14)
plt.ylabel('Relative frequency', fontsize = 14)
plt.tick_params(labelsize = 14)
plt.ylim(0.2,0.8)
plt.grid()
plt.show()

