import timeit

print("1 - Лінійний пошук;\n"  
      "2 - Бінарний пошук;\n"  # Даємо на вибір пошуковий алгоритм
      "3 - Прямий пошук підрядка")
algorithm = int(input("Виберіть пошук: "))

mysetup = '''          # Беремо все у лапки для подальшого тайміта
import numpy as np
import random
            '''
if algorithm == 1:  # Код для лінійного пошуку
    code = '''
lenght = int(input("Введіть к-сть елементів: "))         #задаємо значення довжини масиву
massive = np.zeros(lenght, dtype=int)                    #ініціалізовуємо масив
choice = int(input("Самостійне заповнення(1), Рандомне(2):"))  #даємо рандомне чи самостійне  заповнення
if choice == 1:
    for i in range(lenght):
        element = int(input())
        massive[i] = element                   # Ініціалізовуємо елементи масиву
elif choice == 2:
    for i in range(lenght):
        massive[i] = random.randint(-5, 5)     # Рандомно ініціалізовуємо елементи   
print(massive)
searched = int(input("Введіть шукане число: "))                       # Задаємо шуканий елемент
lenght = len(massive)                        # Потрібно буде щоб перевірити чи буде присутній елемент в вихідному масиві
i = 0
compares = 2 # У найкращому випадку буде 2 порівняння
while i < lenght and massive[i] != searched:  # Поки ми не дійшли кінця списку та поки ми не знайдемо шукане число
    i += 1  
    compares = i * 2
if i == lenght:                               # Якщо ця умова виконалась, то елемент не знайдено
    print("Немає елементу")
else:
    print(f"Елемент {searched} знайдений на позиції {i+1}")  # і+1 щоб позиція була як лічба у нат.числах
    print(f"Було {compares} порівнянь") 
'''
elif algorithm == 2:  # Бінірний пошук
    code = '''
lenght = int(input("Введіть к-сть елементів: "))        # Розмір масиву
massive = np.zeros(lenght, dtype=int)                   # Ініціалізуємо масив
choice = int(input("Самостійне заповнення(1), Рандомне(2):"))
if choice == 1:  #Заповнюємо самі
    for i in range(lenght):
        element = int(input())
        massive[i] = element
elif choice == 2:                                            # Заповнюємо рандомно
    for i in range(lenght):
        massive[i] = random.randint(-5, 5)
searched = int(input("Введіть шукане число: "))              # Шукане число
massive = sorted(massive)                                    # Бінарний пошук працює лише із відсортованими масивами
print(massive)
l_side = 0                 # Наймолодший індекс
r_side = len(massive) - 1  # Найстарший індекс
k = 0
flag = False          # Використовуємо прапорець
while l_side <= r_side and not flag:
    k = (l_side + r_side) // 2           # Середній індекс нашого масиву
    if massive[k] == searched:        # Знайшли елемент,змінюємо значення прапорця
        flag = True
    elif massive[k] < searched:       # Елемент знаходиться праворуч від середини(сунемо ліву межу)
        l_side = k + 1
    else:                             # Елемент праворуч від середини(сунемо праву межу)
        r_side = k - 1
if not flag:
    print('Немає елементу')
else:
    print(f'Елемент {searched} знайдено на {k + 1} позиції')   # k+1 щоб позиція була як лічба у нат.числах
'''
elif algorithm == 3:
    code = '''
string = input()
pattern = input()
i = j = 0
lenS = len(string)  # Довжина стрічки в якій ми шукаєм
lenP = len(pattern)  # Довжина стрічки, яку ми шукаєм
while i <= lenS - lenP and j < lenP:     # поки не досягли одного із кінців
    if string[i + j] == pattern[j]:      # якщо зівпали букви то рухаємось по двум строкам
        j += 1
    else:    # інакше рухаємось по строці(+1), починаючи с 0 символа підстроки
        i += 1
        j = 0
if j == lenP:
    print(f"Підрядок {pattern} починається з {i}")  # якщо дішли до кінца підстроки - знайшли, інакше - ні
else:
    print("Підрядок не знайдено")
    '''
print(timeit.timeit(setup=mysetup,  # Реалізуємо тайміт
                    stmt=code,
                    number=1))
