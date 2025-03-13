import matplotlib.pyplot as plt
import numpy as np

# Experimental configurations and corresponding values
x_values = [1, 2, 4, 8, 16, 32, 64]
y_values = [
    0.9208377003669739 * 100,   # 1
    0.9308117628097534 * 100,   # 2
    0.9413171410560608 * 100,   # 4
    0.9507367014884949 * 100,   # 16
    0.9545990228652954 * 100,   # 32
    95.4                        # 64 (original value kept as percentage)
]

plt.figure(figsize=(10, 6))

# Plot main results
plt.plot(x_values, y_values,
         marker='o',
         linestyle='-',
         linewidth=2,
         markersize=8,
         label='llama-chat-7B')

# Add baseline reference
plt.axhline(y=93.5,
            color='red',
            linestyle='--',
            linewidth=1.5,
            label='logit2text')

# Configure axes
plt.xscale('log', base=2)
plt.xticks(x_values, [str(x) for x in x_values])
plt.xlabel('Number of Outputs', fontsize=12)
plt.ylabel('Cosine Similarity (%)', fontsize=12)
plt.ylim(90, 96)  # Set y-axis limits for better visualization

# Add grid and legend
plt.grid(True,
         which='both',
         linestyle='--',
         alpha=0.7,
         linewidth=0.5)
plt.legend(fontsize=12)

# Add value annotations
for x, y in zip(x_values, y_values):
    plt.annotate(f'{y:.1f}%',
                 (x, y),
                 textcoords="offset points",
                 xytext=(0,5),
                 ha='center')

plt.tight_layout()
plt.show()