import numpy as np
import matplotlib.pyplot as plt
from SALib.sample import saltelli

def Ishigami(x, a=7, b=0.1):
    return np.sin(x[0]) + a * np.sin(x[1])**2 + b * x[2]**4 * np.sin(x[0])

problem = {
    'num_vars': 3,
    'names': ['x1', 'x2', 'x3'],
    'bounds': [[-3.14159265359, 3.14159265359],
               [-3.14159265359, 3.14159265359],
               [-3.14159265359, 3.14159265359]]
}

sample_sizes = 2**np.arange(3, 11)
means = []
variances = []

for size in sample_sizes:
    param_values = saltelli.sample(problem, size)
    Y = np.array([Ishigami(row) for row in param_values])
    means.append(np.mean(Y))
    variances.append(np.var(Y))

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot mean on primary Y-axis
ax1.plot(sample_sizes, means, marker='o', color='blue', label='Mean')
ax1.set_xscale('log')
ax1.set_xlabel('Sample Size')
ax1.set_ylabel('Mean of Output', color='blue')

# Create a secondary Y-axis for variance
ax2 = ax1.twinx()
ax2.plot(sample_sizes, variances, marker='o', color='red', label='Variance')
ax2.set_ylabel('Variance of Output', color='red')

# Title and legend
plt.title('Convergence of Mean and Variance')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()
