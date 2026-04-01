# Use groupby + aggregation (mean, max, etc.)
import pandas as pd
# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)
# Group by 'Category' and calculate the mean of 'Value'
grouped_mean = df.groupby('Category')['Value'].mean()
print(grouped_mean)