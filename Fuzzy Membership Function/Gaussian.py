import numpy as np
import matplotlib.pyplot as plt

def gaussian_mf(x, mean, sigma):
    return np.exp(-((x - mean) ** 2) / (2 * sigma * 2))

x = np.linspace(0, 10, 1000)

m = float(input("Enter mean: "))
s = float(input("Enter sigma: "))
y = gaussian_mf(x, m, s)

plt.plot(x, y, label=f'Gaussian MF (mean={m}, sigma={s})')
plt.xlabel('x values')
plt.ylabel('Membership Degree')
plt.title('Gaussian Membership Function')
plt.legend()
plt.grid()
plt.show()