import pandas as pd
from ydata_profiling import ProfileReport
df =pd.read_csv('/home/opotmans/Langchain/sweetviz/titanic.csv')
report = ProfileReport(df)
report.to_file("my_report.html")