import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y, color='red', linestyle='-', linewidth=2, marker='o', markersize=5)

# Set the x and y axis labels
plt.xlabel('X-axis label', fontsize=12)
plt.ylabel('Y-axis label', fontsize=12)

# Set the title of the plot
plt.title('Plot Title', fontsize=14)

# Add a grid to the plot
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)

# Add a legend to the plot
plt.legend(['sin(x)'], loc='upper left', fontsize=10)

# Show the plot
plt.show()
