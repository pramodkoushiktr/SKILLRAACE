import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate sample data for line plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the line plot
fig, ax = plt.subplots()
ax.plot(x, y1, label='Sine')
ax.plot(x, y2, label='Cosine')
ax.set_title('Sine and Cosine Waves')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xticklabels(['Zero', 'Two', 'Four', 'Six', 'Eight', 'Ten'])
ax.annotate('Local max', xy=(1.5*np.pi, 1), xytext=(4, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Save the line plot
plt.savefig('line_plot.png')
plt.show()

# Generate sample data for bar plots
data = {
    'A': [3, 5, 1, 7],
    'B': [2, 8, 6, 4],
    'C': [5, 7, 3, 6]
}
df = pd.DataFrame(data)

# Create grouped bar plot
df.plot(kind='bar')
plt.title('Grouped Bar Plot')
plt.xlabel('Index')
plt.ylabel('Values')
plt.savefig('grouped_bar_plot.png')
plt.show()

# Create stacked bar plot
df.plot(kind='bar', stacked=True)
plt.title('Stacked Bar Plot')
plt.xlabel('Index')
plt.ylabel('Values')
plt.savefig('stacked_bar_plot.png')
plt.show()
