import pandas as pd
s = pd.Series([2,-1,3,5])
print(s)
#output will be printed with index
import numpy as np
print(np.square(s))
#arithmetic operation on the series
a=s+[1000,2000,3000,4000]
print(a)
#broadcasting
print(s+1000)
#conditional operations
print(s<0)
