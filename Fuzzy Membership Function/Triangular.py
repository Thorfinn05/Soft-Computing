import numpy as np
import matplotlib.pyplot as plt

def triangular_membership(x, a, b, c):
    # if a <= x <= b:
    #     return (x-a)/(b-a)
    # elif b < x < c:
    #     return (c-x)/(c-b)
    # return 0.0
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))


def trapezoidal_membership(x, a, b, c, d):
    if a <= x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1.0
    elif c < x <= d:
        return (d - x) / (d - c)
    return 0.0

def gaussian_membership(x, mean, sigma):
    return np.exp(-((x - mean) ** 2) / (2 * sigma * 2))

x = np.linspace(0, 10, 1000)
#v_triangular = np.vectorize(triangular_membership)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
y = triangular_membership(x, a, b, c)
plt.plot(x, y, label=f"Triangular MF ({a}, {b}, {c})")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Triangular Membership Function")
plt.grid()
plt.legend()
plt.show()

v_trap = np.vectorize(trapezoidal_membership)
d = int(input("Enter d: "))
y = v_trap(x,a,b,c,d)
plt.plot(x, y, label=f"Trapezoidal MF ({a}, {b}, {c}, {d})")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Trapezoidal Membership Function")
plt.grid()
plt.legend()
plt.show()

mean = float(input("Enter mean: "))
sigma = float(input("Enter sigma: "))
y = gaussian_membership(x, mean, sigma)
plt.plot(x, y, label=f"Gaussian MF (m={mean}, s={sigma})")
plt.xlabel("x")
plt.ylabel("m(x)")
plt.title("Gaussian Membership Function")
plt.grid()
plt.legend()
plt.show()