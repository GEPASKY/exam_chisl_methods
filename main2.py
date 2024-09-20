import numpy as np
import matplotlib.pyplot as plt


# Define the function and its derivative
def g(x):
    return (x - 3)**2 + x**2 * np.cos(2 * x)


def g_prime(x):
    return 2 * (x - 3) + 2 * x * np.cos(2 * x) - 2 * x**2 * np.sin(2 * x)


# Initial guess
x0 = 3.5
epsilon = 1e-3
max_iterations = 1000

# Lists to store values for plotting
x_values = []
iterations = []

# Newton-Raphson method
for i in range(max_iterations):
    x_values.append(x0)
    iterations.append(i)
    x1 = x0 - g(x0) / g_prime(x0)
    if abs(x1 - x0) < epsilon:
        x0 = x1
        break
    x0 = x1

root = x0
print(f"Приближенное значение корня: {root:.3f}")
print(f"Количество итераций: {i + 1}")

# Plotting the convergence
plt.plot(iterations, x_values)
plt.title("Конвергенция метода Ньютона-Рафсона")
plt.xlabel("Итерации")
plt.ylabel("Приближение значения корня")
plt.show()
