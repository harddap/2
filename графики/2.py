import matplotlib.pyplot as plt
import numpy as np

def function_1(x):
    return 6*x**3 - 2*x + 8

def function_2(x):
    return 3*x + 1

x_values = np.linspace(-10, 10, 100)

y_values_1 = function_1(x_values)
y_values_2 = function_2(x_values)

plt.plot(x_values, y_values_1, label='F(x, y) = 6x**3 - 2x + 8')
plt.plot(x_values, y_values_2, label='F(x, y) = 3x + 1')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функций')
plt.legend()

plt.show()