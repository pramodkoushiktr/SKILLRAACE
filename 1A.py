#i) Data Cleaning

import pandas as pd
import numpy as np

# Creating a DataFrame with missing data
data = {
    'A': [1, 2, np.nan, 4, 5, np.nan, 7],
    'B': ['a', 'b', 'b', np.nan, 'e', 'f', 'f'],
    'C': [np.nan, 2, 3, 4, 5, 6, 7],
    'D': [1, 2, 3, 4, 4, 4, 7]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Identifying missing data
print("\nMissing data identified (True indicates missing data):")
print(df.isna())

# Filtering out rows with any missing data
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with any missing data:")
print(df_dropped)

# Filling missing data
df_filled = df.fillna({
    'A': df['A'].mean(),  # Fill missing 'A' with mean
    'B': 'unknown',       # Fill missing 'B' with 'unknown'
    'C': df['C'].median() # Fill missing 'C' with median
})
print("\nDataFrame after filling missing data:")
print(df_filled)

# Identifying duplicates
print("\nDuplicate rows identified (True indicates duplicate):")
print(df.duplicated())

# Removing duplicates
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after removing duplicate rows:")
print(df_no_duplicates)

#ii) Hierarchical Indexing
# Creating a Series with a hierarchical index
arrays = [
    ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c'],
    [1, 2, 3, 1, 2, 3, 1, 2]
]
index = pd.MultiIndex.from_arrays(arrays, names=('outer', 'inner'))
data = [0, 1, 2, 3, 4, 5, 6, 7]
s = pd.Series(data, index=index)
print("\nSeries with hierarchical index:")
print(s)

# Selecting subsets of data at the outer level
print("\nData subset for outer level 'a':")
print(s['a'])

# Selecting subsets of data at the inner level
print("\nData subset for outer level 'a' and inner level 2:")
print(s['a', 2])

# Selecting subsets of data for the entire hierarchical index
print("\nData subset for outer level 'b' and inner level 1:")
print(s['b', 1])
