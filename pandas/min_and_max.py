# Find minimum/maximum per group
import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# Group by 'Category' and find the minimum of 'Value'
grouped_min = df.groupby('Category')['Value'].min()
print("Minimum values per group:")
print(grouped_min)

# Group by 'Category' and find the maximum of 'Value'
grouped_max = df.groupby('Category')['Value'].max()
print("Maximum values per group:")
print(grouped_max)