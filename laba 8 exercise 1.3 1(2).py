import numpy as np

a = np.zeros((3, 3), dtype=int)  # Ініціалізуємо масив 3х3
for i in range(3):      # Створюємо
    for j in range(3):  # цикли для заповнення масиву
        a[i, j] = int(input())
print('Вхідна матриця:', end='\n' f'{a}''\n')
b = np.zeros((3, 3), dtype=int)  # Ініціалізуємо ще один масив 3х3'
for i in range(3):         # Трансонована матриця це матриця
    for j in range(3):     # в якій на місце рядків стають стовпці
        b[i, j] = a[j, i]  # Отже, просто міняємо їх місцями
print('Трансонована матриця:', end='\n' f'{b}')
