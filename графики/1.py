import matplotlib.pyplot as plt
import numpy as np

def linear_function(x):
    return 6*x - 2

x_values = np.linspace(-10, 10, 100)

y_values = linear_function(x_values)

plt.plot(x_values, y_values, label='y = 6x - 2')

plt.xlabel('x')
plt.ylabel('y')
plt.title('График линейной функции')
plt.legend()
plt.show()




