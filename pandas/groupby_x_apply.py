# Use groupby + apply
import pandas as pd
# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# Use groupby + apply to calculate the mean of 'Value' for each group
grouped_mean = df.groupby('Category')['Value'].apply(lambda x: x.mean())
print("Mean values per group:")
print(grouped_mean)