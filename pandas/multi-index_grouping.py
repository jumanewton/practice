# Handle multi-index grouping
import pandas as pd
# Sample DataFrame with multi-index
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)
df = df.set_index(['Category', 'Subcategory'])
# Group by multi-index and calculate the sum of 'Value'
grouped_sum = df.groupby(level=['Category', 'Subcategory'])['Value'].sum()
print("Sum of values per multi-index group:")
print(grouped_sum)
# Group by multi-index and calculate the mean of 'Value'
grouped_mean = df.groupby(level=['Category', 'Subcategory'])['Value'].mean()
print("Mean of values per multi-index group:")
print(grouped_mean)

# Group by multi-index and calculate the count of 'Value'
grouped_count = df.groupby(level=['Category', 'Subcategory'])['Value'].count()
print("Count of values per multi-index group:")
print(grouped_count)
# Group by multi-index and calculate the max of 'Value'
grouped_max = df.groupby(level=['Category', 'Subcategory'])['Value'].max()
print("Max of values per multi-index group:")
print(grouped_max)
# Group by multi-index and calculate the min of 'Value'
grouped_min = df.groupby(level=['Category', 'Subcategory'])['Value'].min()
print("Min of values per multi-index group:")
print(grouped_min)

