import numpy as np
import matplotlib.pyplot as plt


# Number of noise trials
noiseTrials = 1000

# This function checks to see if there are any values in a numpy array that
# are repeated. If there are then it returns a 1. If there are no repeats
# then it returns no repeats
def isThereAMatch(t):
    # Returns the indices of values
    u, i = np.unique(t, return_inverse=True);
    # Check to see if any value the bincount is larger than 1
    p = np.sum(np.bincount(i) > 1)
    if p > 0:
    	return 1
    else:
    	return 0

# This function computes the probability for a match given N students
# out of noiseTrial noise trials
def probForThisN(N,noiseTrials):
    # Run the noise trials loop
    # This loop runs the random draw experiment noiseTrials times
    sC = 0;
    for noiseInd in range(1,noiseTrials+1):
        t = np.sort(np.random.randint(1,365,N));    
        # print(isThereAMatch(t))
        if isThereAMatch(t) == 1:
            sC += 1;
    # The number of experiments that ended up having at least 1 matching number
    #print(sC)
    #print(noiseInd)
    probForN = sC/noiseInd;
    # print('The probability for this {} of students is {}'.format(N,probForN))
    return probForN

print('Running please wait...')

# This for loop calculates the probably of the same birthday for N number
# of students and stores the probabilities in an array
Nlist = np.arange(1,101);
probVsN = np.empty([100]);
for Nind in Nlist:
    tempVar = probForThisN(Nind, noiseTrials)
    probVsN[Nind - 1] = tempVar; 

# Plot the probability of the same birthday vs N number of students
plt.plot(Nlist,probVsN);
plt.grid()
plt.show()
