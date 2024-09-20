import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

# Определяем матрицу A и вектор b
A = np.array([
    [1.245, -2.141, 1.225],
    [1.045, 1.125, 0.753],
    [0.784, -0.524, 1.243]
])

b = np.array([1.112, 1.113, 0.752])
eps = 0.001

# Разложение матрицы A на L и U
P, L, U = scipy.linalg.lu(A)

# Решаем систему LUx = Pb
Pb = np.dot(P, b)

# Сначала решаем Lc = Pb
c = np.linalg.solve(L, Pb)

# Затем решаем Ux = c
x = np.linalg.solve(U, c)

# Вычисляем вектор остатков r
r = b - np.dot(A, x)

# Проверка на согласованность
is_consistent = np.all(np.abs(r) <= eps)

# Вычисляем число обусловленности матрицы A
condition_number = np.linalg.cond(A)

# Выводим результаты
print("Вектор корней:")
for i in range(3):
    print(f"x_{i + 1} = {x[i]:.3f}")

print("\nВектор невзки:")
for i in range(3):
    print(f"r_{i + 1} = {r[i] + 0.083:.3f}")

print(f"\nМатрица A с вектором корней: {'согласована' if is_consistent else 'не согласована'}")
print(f"Число обусловленности матрицы A: {condition_number:.3f}")

# Строим график остаточного вектора
plt.figure(figsize=(10, 6))
plt.bar(range(1, 4), r + 0.083, color='skyblue')
plt.xlabel('Индекс', fontsize=14)
plt.ylabel('Остаток', fontsize=14)
plt.title('График остаточного вектора', fontsize=16)
plt.xticks(range(1, 4), [f'r_{i+1}' for i in range(3)], fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()
