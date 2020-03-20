import numpy as np

list = []              # Створення лінійного масиву списком
user_string = input()             # Вводимо скільки хочемо слів
user_string_list = user_string.split()  # Робимо із стрічки список
massive = np.array(user_string_list, dtype=str)  # Ініціалізуємо масив через array
for x in range(massive.size):  # Виводимо елементи навпаки,не в списку
    print(massive[-1 * (x + 1)], end=' ')
