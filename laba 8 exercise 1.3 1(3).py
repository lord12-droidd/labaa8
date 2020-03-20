import numpy as np

a = np.zeros((3, 3), dtype=int)  # Створюємо 1 матрицю
for i in range(3):
    for j in range(3):
        a[i, j] = int(input())
print('Вхідна матриця 1:', end='\n' f'{a}''\n')
b = np.zeros((3, 3), dtype=int)  # Створюємо 2 матрицю
for i in range(3):
    for j in range(3):
        b[i, j] = int(input())
print('Вхідна матриця 2:', end='\n' f'{b}''\n')
c = np.zeros((3, 3), dtype=int)  # Ініціалізуємо матрицю, яка буде результатом
for i in range(3):  # Виконуємо МАТРИЧНИЙ добуток
    for j in range(3):   # (кожен рядок 1 матриці перемножуємо на кожен стовпчики 2 матриці)
        for k in range(3):  # і так кожен раз по 3 рази
            c[i][j] += a[i][k] * b[k][j]
print('Результат: ''\n', c)
