
import numpy as np
import pandas as pd

#import the datetime library used by Panda for time series data

import matplotlib.pyplot as plt

#create a serie of number
s1 = pd.Series ([1,2,3,4])
print(s1)

dates = pd.date_range ('2017-04-01','2017-04-04')
print (dates)

temp1 = pd.Series([80,81,82,83],index=dates)
print (temp1)
