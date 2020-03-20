while True:  # 2 Вайла для трая і зациклення программи
    while True:
        Info_makers = {
            'Intel': {'Intel Core i3': 132, 'Intel UHD Graphics 620': 168},
            'Asus': {'Asus P8H61-M LX3 R2.0': 82},
            'Samsung': {'SAMSUNG 1 TB': 43},  # Створення вкладеного словника із даними для 1 пункту
            'Seagate': {'SEAGATE IRONWOLF': 34},
            'Focusrite': {'Focusrite Scarlett 6i6 MK2': 56}
        }
        Info_objects = {
            "Processor": {'Intel': 132},
            "Motherboard": {'Asus': 82},
            'Memory': {'SAMSUNG': 43},  # Створення вкладеного словника для 2 пункту
            'Videocard': {'Intel': 168},
            'Soundcard': {'Seagate': 34},
            'HDD': {'Focusrite': 56}
        }
        search_maker = input('Enter maker: ')  # Введення назви виробника
        search_object = input('Enter object of PC: ')  # Введення назви складової комп'ютера
        makers = ['Intel', 'Samsung', 'Asus', 'Seagate', 'Focusrite']                      # Створення списків
        objects = ["Processor", "Motherboard", 'Memory', 'Videocard', 'Soundcard', 'HDD']  # із ключами словників
        try:
            for info in makers:           # Перебираємо ключі словника для виробників
                if info == search_maker:  # Потім перевіпяємо на збіг із запитом
                    print(info, Info_makers[info])
            for info in objects:           # Перебираємо ключі словника для складових комп'ютера
                if info == search_object:  # Перевіряємо на збіг із запитом
                    print(info, Info_objects[info])
        except KeyError:                     # Якщо виробник або складова введена неправильно
            print("No info found")           # або просто немає такої то спрацьовує кейерор який ми перехвачуємо
        print(f'If you want to exit {exit}')
        leave = input()
        if leave == 'exit':
            break
