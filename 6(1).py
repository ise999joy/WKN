from math import * # імпортуємо всі функції з модуля math

# Зайві коментарі видаліть перед захистом проекту!!!!!

# Отримуємо а, b, h від користувача
a = float(input("Введите а: ")) 
b = float(input("Введите b: ")) 
h = float(input("Введите h: "))

x = a # Присвоюємо х значення нижньої границі нашого діапазону

# Создаємо цикл з параметром
for i in range(10000):

    # Визначаємо у для значення х та округлюємо одразу до 4 знаків після коми
    y = round((1 / (x * x + 1)) + x * x, 4) # x*x те саме, що й х в другій степені 
    x = round(x, 4) # округлюємо х, щоб мати більш гарний вигляд

    print("x = " + str(x) + " - " + "y = " + str(y)) # можна викорастати кращий варіант print(f"x = {x} - y = {y}") але можуть не повірити, що написали власноруч
    

    # додаємо до поточного значення х шаг h
    x = x + h # можна написати x += h

    # Робимо умову, коли х стане більшим за верхню межу діапазону прервемо роботу циклу
    if x > b:
        break