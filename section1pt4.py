import numpy as np

# This code simulates the tossing of a coin 4 times with the probability of a heads 
# being 75% and the probability of a tails being 25%

#s = np.random.uniform(0,1,1)
#print(s)

number = 0
x = []

for i in range(1,5):
	
	if np.random.uniform(0,1,1) < 0.75: # Toss Coin With p = 0.75
	    x.append(1)
	else:
	    x.append(0)
	    
	number = number + x[i-1]

print(x)    
print(number)


