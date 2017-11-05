
import numpy as np
import pandas as pd

#import the datetime library used by Panda for time series data
import matplotlib.pyplot as plt

#adapt the display of pandas via options
pd.set_option ('display.notebook_repr_html', False)
pd.set_option ('display.max_columns',16)
pd.set_option('display.max_rows',10)
pd.set_option('display.width',200)

#Definition of the Serie with Pandas
#===================================

#create a serie of number
s1 = pd.Series ([1,2,3,4])
print(s1)

#Create a serie of times with start and end, possible to define the frequencies
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

#Create a dataframe based on a CSV : Extract file of csv
# on the file marx-geo.csv there is fields number error ==> I use the option error_bad_lines=False to bypass these errors
# Seeing that this is a timeseries, I use the first column as datetime as the index: this is the option index_col='datetime'
marx = pd.read_csv ('c:/users/opotmans/Downloads/marx-geo.csv',error_bad_lines=False,index_col='datetime')
print(marx.head())
#to display the index of the dataframe (marx)
print(marx.index)

