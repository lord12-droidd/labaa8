import numpy as np

a = np.zeros((4, 4), dtype=int)  # Створюємо масив 4х4
for i in range(4):
    for j in range(4):
        a[i, j] = int(input(f'A[{i},{j}]= '))  # Заповнюємо його
        if a[i, j] < 0:  # при кожній ітерації перевіряємо його на від'ємність
            a[i, j] = 0  # якщо від'ємний то міняємо елемент на 0
print(a)
