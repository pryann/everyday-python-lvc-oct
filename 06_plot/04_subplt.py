import matplotlib.pyplot as plt
import numpy as np

data_1 = np.random.normal(0, 1, 1000)
data_2 = np.random.normal(3, 2, 1000)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(data_1, bins=25, color="blue", alpha=0.7)
ax1.set_title("Normal Distribution (mean=0, std=1)")
ax1.set_xlabel("Value")
ax1.set_ylabel("Frequency")
ax1.grid(True, alpha=0.3)

ax2.hist(data_2, bins=25, color="red", alpha=0.7)
ax2.set_title("Normal Distribution (mean=3, std=2)")
ax2.set_xlabel("Value")
ax2.set_ylabel("Frequency")
ax2.grid(True, alpha=0.3)

fig.suptitle("Comparison of Two Normal Distributions", fontsize=16)
plt.tight_layout()
plt.savefig("comparison_normal_distributions.png")
plt.show()
