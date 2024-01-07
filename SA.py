from SALib.analyze import morris
from SALib.sample.morris import sample
from SALib.analyze import fast
from SALib.sample import fast_sampler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

problem = {
 'num_vars': 8,
 'names': ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8'],
 'bounds': [[0.0, 1.0],
            [0.0, 1.0],
            [0.0, 1.0],
            [0.0, 1.0],
            [0.0, 1.0],
            [0.0, 1.0],
            [0.0, 1.0],
            [0.0, 1.0]]
}

def sobol_g_function(params):
    a = [78, 12, 0.5, 2, 97, 33, 11, 90]
    product = 1
    for i in range(len(params)):
        product *= (abs(4 * params[i] - 2) + a[i]) / (1 + a[i])
    return product


param_values = sample(problem, N=1000, num_levels=4, optimal_trajectories=None)
Y = np.array([sobol_g_function(sample) for sample in param_values])
Si_morris = morris.analyze(
    problem,
    param_values,
    Y,
    conf_level=0.95,
    print_to_console=False,
    num_levels=4,
    num_resamples=100)

param_values = fast_sampler.sample(problem, 1000, seed=100)
Y = np.array([sobol_g_function(sample) for sample in param_values])
Si_fast = fast.analyze(problem, Y, print_to_console=False, seed=100)


morris_data = pd.DataFrame(Si_morris)
fast_data = pd.DataFrame(Si_fast)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
# Morris Method Bar Plot with annotation
morris_bar = ax1.bar(morris_data['names'], morris_data['mu_star'], yerr=morris_data['sigma'], capsize=5)
ax1.set_xlabel('Variables')
ax1.set_ylabel('Mu* (mu_star)')
ax1.set_title('Morris Method Sensitivity Analysis')
ax1.grid(True)
ax1.text(0.7, 0.95, 'Vertical strokes represent sigma values', horizontalalignment='center', 
         verticalalignment='center', transform=ax1.transAxes, fontsize=12, color='blue')

# Fast Method Bar Plot
bar_width = 0.35
r1 = range(len(fast_data))
r2 = [x + bar_width for x in r1]
fast_bar1 = ax2.bar(r1, fast_data['S1'], width=bar_width, label='S1')
fast_bar2 = ax2.bar(r2, fast_data['ST'], width=bar_width, label='ST')
ax2.set_xlabel('Variables')
ax2.set_xticks([r + bar_width / 2 for r in range(len(fast_data))])
ax2.set_xticklabels(fast_data['names'])
ax2.set_ylabel('Sensitivity Indices')
ax2.set_title('Fourier Amplitude Sensitivity Testing (FAST) Sensitivity Analysis')
ax2.legend()

plt.tight_layout()
plt.show()