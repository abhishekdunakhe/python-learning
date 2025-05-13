import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('module 4/Placement_Dataset.csv')
print(dataset.head())
# print(dataset.isnull().sum())
# print(dataset.shape)
# dataset['salary'].fillna(dataset['salary'].median(), inplace=True)
# dataset['salary'].fillna(dataset['salary'].mean(), inplace=True)
# dataset['salary'].fillna(dataset['salary'].mode(), inplace=True)

# print(dataset.head())
# print(dataset.isnull().sum())


salary_dataset = pd.read_csv('module 4/Placement_Dataset.csv')

salary_dataset = salary_dataset.dropna(how="any")
print(salary_dataset.isnull().sum())
print(salary_dataset.shape)

