import random
import numpy as np
inp = int(input("How many numbers? "))
fileName = input("Filename (no extension)? ")
dataSet = []

for i in range(0, inp-1):
	dataSet.append(random.randint(0, 5000000))
#np.savetxt('{}.txt'.format(fileName), dataSet, delimiter="\n", fmt="%s")
ds = np.array(dataSet)
np.savetxt('{}.csv'.format(fileName), [ds], delimiter=',', fmt='%d')
'''
with open('{}.txt'.format(fileName), 'w') as f:
    for item in dataSet:
        f.write("%s " % item)
'''