# Perform sorting operations
import numpy as np
import pandas as pd
# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
# Sort by Age in ascending order
sorted_by_age = df.sort_values(by='Age')
print("DataFrame sorted by Age (ascending):")
print(sorted_by_age)
# Sort by Salary in descending order
sorted_by_salary = df.sort_values(by='Salary', ascending=False)
print("DataFrame sorted by Salary (descending):")
print(sorted_by_salary)
# Sort by multiple columns: first by Age (ascending), then by Salary (descending)
sorted_by_age_salary = df.sort_values(by=['Age', 'Salary'], ascending=[True, False])
print("DataFrame sorted by Age (ascending) and Salary (descending):")
print(sorted_by_age_salary)
# Sort by index
sorted_by_index = df.sort_index()
print("DataFrame sorted by index:")
print(sorted_by_index)
# Sort by index in descending order
sorted_by_index_desc = df.sort_index(ascending=False)
print("DataFrame sorted by index (descending):")
print(sorted_by_index_desc)
# Sort by values in a specific column and handle missing values
data_with_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, np.nan, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df_with_nan = pd.DataFrame(data_with_nan)
# Sort by Age, handling missing values
sorted_by_age_nan = df_with_nan.sort_values(by='Age', na_position='last')
print("DataFrame sorted by Age (with missing values handled):")
print(sorted_by_age_nan)

