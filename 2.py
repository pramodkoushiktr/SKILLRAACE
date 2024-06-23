import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
np.random.seed(42)
data = np.random.normal(loc=50, scale=15, size=1000)
data1 = np.random.normal(loc=50, scale=15, size=1000)
data2 = np.random.normal(loc=55, scale=10, size=1000)
categories = np.random.choice(['Category 1', 'Category 2', 'Category 3', 'Category 4'], size=1000)

# Create a DataFrame for box plot
df = pd.DataFrame({'Value': data, 'Category': categories})

# Plotting
plt.figure(figsize=(15, 10))

# i) Histogram and Density Plot
plt.subplot(2, 2, 1)
sns.histplot(data, kde=True)
plt.title('Histogram and Density Plot')

# ii) Scatter Plot
plt.subplot(2, 2, 2)
plt.scatter(data1, data2, alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('Data1')
plt.ylabel('Data2')

# iii) Box Plots
plt.subplot(2, 2, 3)
sns.boxplot(x='Category', y='Value', data=df)
plt.title('Box Plot')

plt.tight_layout()
plt.show()
