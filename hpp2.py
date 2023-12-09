import string
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Data/DataSet.xlsx', sheet_name='FilteredData')

#convert LA_N and RA_N to float and remove those that cannot be changed
df['LA_N'] = pd.to_numeric(df['LA_N'], errors='coerce')
df['RA_N'] = pd.to_numeric(df['RA_N'], errors='coerce')
#coerce-> converts non-convertible values to NaN/null

df.dropna(subset=['LA_N','RA_N','FACING_N'],inplace=True)
#subset parameter allows us to specify multipe columns

#data cleaned as of now, now visualisation
#1. correlation matrix/heatmap
#2. boxplot to visualise outliers
#3. scatterplot, relation between price vs land area,roadsize,built year
#4 time serises plot, to visualise the no of properties built per year

#correlation heatmap cannot be created without a correlation matrix
cor_matrix=df[['LA_N','RA_N','BY_N','FACING_N','BEDROOM','BATHROOM','FLOOR','PRICE_N']].corr()

#plt.figure(figsize=(8,6))
#sns.heatmap(cor_matrix,annot=True,cmap='coolwarm',fmt='.2f',annot_kws={"size":10})
#plt.title('Correlation Heatmap')
#plt.show()

plt.figure(figsize=(8,6))
sns.countplot(df,x='BY_N',palette='viridis')
plt.title('Houses Built per Year')
plt.xlabel('Categories')
plt.ylabel('Frequency')
plt.show()