
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
temp2= pd.Series ([70,71,72,73],index=dates)
temps_diff = temp1-temp2
print (temps_diff)
print (temps_diff.mean())
temps_df = pd.DataFrame({'brussels' : temp1, 'namur': temp2})
print (temps_df)