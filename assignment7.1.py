
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

print(moving_average([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]))  
print("length of moving average is")
print(len(moving_average([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])))

