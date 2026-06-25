"""
How do we represent a coin?
0 = Tail
1 = Head

"""
import numpy as np
#Instead of one flip, generate 10.
flip = np.random.choice([0,1],10)
print(flip)

heads = np.sum(flip)

print(heads)