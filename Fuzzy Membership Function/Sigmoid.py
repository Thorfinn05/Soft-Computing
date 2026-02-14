import numpy as np
import matplotlib.pyplot as plt

def sigmoid_mf(x, a, c):
    return (1 / (1 + np.exp(-a * (x - c))))

x = np.linspace(-10, 10, 100)

a = float(input('Enter slope: '))
c = float(input('Enter centre: '))
y = sigmoid_mf(x, a, c)

plt.plot(x, y, label=f'Sigmoid MF\nSlope={a}, Centre={c}')
plt.title('Sigmoid Membership Function')
plt.xlabel('x values')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid()
plt.show()