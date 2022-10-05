import random

n = int(input("Введіть кількість номерів для генерації: "))
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ids = []
i = 0

while i < n:

    first_char = random.choice(ABC)
    second_char = random.choice(ABC)
    third_char = random.choice(ABC)

    number = random.randint(10000, 99999)

    s = str(first_char) + str(second_char) + str(third_char) + " " + str(number)

    if s in ids:
        continue
    else:
        ids.append(s)
        i = i + 1
