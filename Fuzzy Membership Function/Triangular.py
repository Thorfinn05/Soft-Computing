import numpy as np
import matplotlib.pyplot as plt

def triangular_membership(x, a, b, c):
    # if a < x <= b:
    #     return (x-a)/(b-a)
    # elif b < x < c:
    #     return (c-x)/(c-b)
    # return 0.0
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

x = np.linspace(0, 10, 1000)

#v_triangular = np.vectorize(triangular_membership)
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
y = triangular_membership(x, a, b, c)
plt.plot(x, y, label=f"Triangular MF ({a}, {b}, {c})")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Triangular Membership Function")
plt.grid()
plt.legend()
plt.show()
