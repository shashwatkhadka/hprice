import string
import pandas as pd

df = pd.read_excel('Data/DataSet.xlsx', sheet_name='FilteredData')

#convert LA_N and RA_N to float and remove those that cannot be changed
df['LA_N'] = pd.to_numeric(df['LA_N'], errors='coerce')
df['RA_N'] = pd.to_numeric(df['RA_N'], errors='coerce')
#coerce-> converts non-convertible values to NaN/null

df.dropna(subset=['LA_N','RA_N','FACING_N'],inplace=True)
#subset parameter allows us to specify multipe columns

#data cleaned as of now, now visualisation
print(df.info())
#1. correlation matrix/heatmap
#2. boxplot to visualise outliers
#3. scatterplot, relation between price vs land area,roadsize,built year
#4 time serises plot, to visualise the no of properties built per year
#5.