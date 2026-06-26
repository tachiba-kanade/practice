"""
How do we represent a coin?
0 = Tail
1 = Head

"""
import numpy as np
from scipy.stats import norm
#Instead of one flip, generate 10.\

res = []
for i in range (5000):
    flip = np.random.choice([0,1],10000)
    print(flip)
    heads = np.sum(flip)
    print(heads)
    res =np.append(heads)

print(res)

probabilty  = np.mean(np.array(res)>5200)

import matplotlib.pyplot as plt
plt.hist(res)
plt.show()


"""
Probability theory
Python programming
Simulation (Monte Carlo)
Statistical inference (Central Limit Theorem)

"""



