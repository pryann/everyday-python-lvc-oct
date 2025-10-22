import matplotlib.pyplot as plt
import numpy as np

mean = 0
std = 1
data = np.random.normal(mean, std, 1000)

plt.hist(data, bins=25, density=True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Normal Distribution (mean=0, std=1)")
plt.show()
