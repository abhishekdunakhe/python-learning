import pandas as pd
from sklearn.datasets import fetch_openml
import numpy as np

openml_datasets = fetch_openml(name="house_prices", as_frame=True)
# print(type(openml_datasets)) # <class 'sklearn.utils._bunch.Bunch'>
# print(openml_datasets)

# python dataframe.
openml_df = pd.DataFrame(openml_datasets.data, columns= openml_datasets.feature_names)
# print(openml_df.head())
# print(openml_df.shape)
# print(type(openml_df)) #<class 'pandas.core.frame.DataFrame'>

diabetes_df = pd.read_csv('diabetes.csv')
# print(type(diabetes_df)) #<class 'pandas.core.frame.DataFrame'>
# print(type(diabetes_df))
# print(diabetes_df.head())
# print(diabetes_df.shape)

print(openml_df.to_csv('openml.csv'))

random_df = pd.DataFrame(np.random.rand(5,5))
# print(random_df)

# print(openml_df.head()) # this gives first 5 rows 
# print(openml_df.tail()) # this gives last 5 rows 
# print(openml_df.info()) # this gives info rows 
# print(openml_df.isnull().sum()) # this gives number of missing values in each column in typical dataframe. 

# print(diabetes_df.value_counts('Age'))
# print(diabetes_df.groupby('Outcome').mean()) # it give mean value of each column
# print(diabetes_df.count()) # count in each column
# print(diabetes_df.mean()) # mean value column vise
# print(diabetes_df.std()) # this gives standard deviation value from col
# print(diabetes_df.max())  # this gives max value from col
# print(diabetes_df.min()) # this gives min value from col
# print(diabetes_df.describe()) # this gives all the detail of value from dataframe
# openml_df['hi'] = openml_datasets.feature_names # thsi is use to add new column in table
# print(openml_df.drop(index=0, axis=0)) # thiss will drop row from datasets index is row number and axis is col value
# print(openml_df.drop(columns="MSSubClass", axis=1))
# print(openml_df.iloc[3]) # this will gives specific row value mention in [].
# print(openml_df.iloc[:,0]) # first column
# print(openml_df.iloc[:,1]) # first column
# print(openml_df.iloc[:,2]) # second column
# print(openml_df.iloc[:,-1]) # last column
correlation_matrix = openml_df.corr() # this is used for correlation in table.
print(correlation_matrix)
