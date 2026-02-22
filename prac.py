import numpy as np
import matplotlib.pyplot as plt

def triangular_membership(x, a,b,c,d):
    # 
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

x = np.linspace(0, 10, 1000)

v_triangular = np.vectorize(triangular_membership)
y = v_triangular(x, 2.0, 4.0, 8.0)
plt.plot(x, y)
plt.fill_between(x,y,alpha=0.3)
plt.grid(); plt.show()

