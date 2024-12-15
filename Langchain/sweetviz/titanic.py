import pandas as pd
import sweetviz as sv
df =pd.read_csv('/home/opotmans/Langchain/sweetviz/titanic.csv')
df.head()
report = sv.analyze(df)
report.show_html('report.html')