import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_mf(x, a, b, c, d):
    if a <= x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1.0
    elif c < x <= d:
        return (d - x) / (d - c)
    return 0.0

x = np.linspace(0, 10, 1000)    
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))

v_trap = np.vectorize(trapezoidal_mf)
y = v_trap(x, a, b, c, d)

plt.plot(x, y, label=f'Trapezoidal MF ({a}, {b}, {c}, {d})')
plt.title('Trapezoidal Membership Function')
plt.xlabel("x values")
plt.ylabel('Mmbership Degree')
plt.legend()
plt.grid()
plt.show()