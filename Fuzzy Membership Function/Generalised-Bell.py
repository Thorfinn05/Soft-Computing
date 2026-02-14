import numpy as np
import matplotlib.pyplot as plt

def generalisd_bell_mf(x, a, b, c):
    return 1 / (1 + np.abs((x - c) / a) ** (2 * b))

x = np.linspace(0, 10, 1000)

a = float(input("Enter width: "))
b = float(input("Enter slope: "))
c = float(input("Enter centre: "))
y = generalisd_bell_mf(x, a, b, c)

plt.plot(x, y, label=f'width={a}\nslope={b}\ncentre={c}')
plt.xlabel('x values')
plt.ylabel('Membership Degree')
plt.title("Generalised Bell Mmbership Function")
plt.legend(); plt.grid()
plt.show() 