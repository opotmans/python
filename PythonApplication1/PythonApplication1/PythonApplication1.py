
import numpy as np
import pandas as pd
import datetime
#import timeit for the measure of execution
import timeit

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
#using a python list
s1 = pd.Series ([1,2,3,4])
print(s1)
#using numpy 
s2 = pd.Series (np.arange(4,9))
print (s2)
#using random number of numpy
np.random.seed(12345)
s3 = pd.Series(np.random.normal(size=5))
print(s3)

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

#reindexation of a series
s3.index = ['a','b','c','d','e']
print (s3)
s3= s3.reindex([1,2,3,4,5])
print (s3)

#reindexation by interpolating the values between the holes


#Create a dataframe based on a CSV : Extract file of csv
# on the file marx-geo.csv there is fields number error ==> I use the option error_bad_lines=False to bypass these errors
# Seeing that this is a timeseries, I use the first column as datetime as the index: this is the option index_col='datetime'
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
marx = pd.read_csv ('c:/users/opotmans/Downloads/marx-geo.csv',error_bad_lines=False,index_col='datetime')
print(marx.head())
#to display the index of the dataframe (marx)
print(marx.index)

#measure importance of the index in pandas with timeit
np.random.seed(123456)
df= pd.DataFrame({'foo':np.random.random(10000),'key':range(100,10100)})
print (df[:5])

#use the class timeit to calculate the execution time
# error in the "learning pandas" book: the working of timeit is not correctly used 
timeit.timeit(stmt='df[:3]',setup='import pandas as pd;import numpy as np; np.random.seed(123456);df= pd.DataFrame({"foo":np.random.random(10000),"key":range(100,10100)})')
df_with_index = df.set_index(['key'])
print(timeit.timeit (setup='pass',stmt='print(df_with_index.loc[10099])'))



