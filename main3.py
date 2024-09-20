import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (x - 3) * 2 + x * 2 * np.cos(2 * x)


def df(x):
    return 2 * (x - 3) + 2 * x * np.cos(2 * x) - 4 * x * np.sin(2 * x)


def tangent_method(x0, epsilon):
    iterations = 0
    x_history = [x0]

    while True:
        iterations += 1
        x1 = x0 - f(x0) / df(x0)
        x_history.append(x1)
        if abs(x1 - x0) <= epsilon:
            break
        x0 = x1

    print(f"Приближенное значение корня: {x1:.3f}")
    print(f"Количество итераций: {iterations}")
    print(f"Погрешность: {abs(x1 - x0):.3f}")

    return x1, iterations, x_history


# Начальное приближение и точность
x0 = 2.5
epsilon = 1e-3

# Вызываем метод касательных
root, iterations, x_history = tangent_method(x0, epsilon)

# Построение графиков
x = np.linspace(0, 5, 400)
y = f(x)

plt.figure(figsize=(12, 6))

# График функции f(x)
plt.subplot(121)
plt.plot(x, y, label='$f(x)=(x-3)*2 + x*2*cos(2*x)$')
plt.axhline(0, color='black', linewidth=0.5)
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# График корней и итераций
plt.subplot(122)
plt.plot(x, y, label='$f(x)$')
plt.scatter(x_history, f(np.array(x_history)), color='red', label='Корни')
plt.axhline(0, color='black', linewidth=0.5)
plt.title('График корней и итераций')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.tight_layout()
plt.show()
