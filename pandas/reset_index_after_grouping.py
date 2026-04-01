# Reset index after grouping
import pandas as pd
# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)
# Group by 'Category' and calculate the sum of 'Value'
grouped_sum = df.groupby('Category')['Value'].sum().reset_index()
print("Sum of values per category with reset index:")
print(grouped_sum)
# Group by 'Category' and calculate the mean of 'Value'
grouped_mean = df.groupby('Category')['Value'].mean().reset_index()
print("Mean of values per category with reset index:")
print(grouped_mean)
# Group by 'Category' and calculate the count of 'Value'
grouped_count = df.groupby('Category')['Value'].count().reset_index()
print("Count of values per category with reset index:")
print(grouped_count)
# Group by 'Category' and calculate the max of 'Value'
grouped_max = df.groupby('Category')['Value'].max().reset_index()
print("Max of values per category with reset index:")
print(grouped_max)
# Group by 'Category' and calculate the min of 'Value'
grouped_min = df.groupby('Category')['Value'].min().reset_index()
print("Min of values per category with reset index:")
print(grouped_min)
