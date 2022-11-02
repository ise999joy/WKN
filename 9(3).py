45
planets = ("Меркурій", "Венера", "Земля", "Марс", "Юпітер", "Сатурн", "Уран", "Нептун")
planets_radiuses = {}


for i in planets:
    radius = float(input(f"Введіть радіус планеты {i}(км): "))

    
    planets_radiuses[i] = radius


while True:
    
    s = input("Введіть назву планети для знаходження її радіуса або порожню строку для завершення пошуку: ").lower().capitalize()
    
    if s == "":
        break

    
    if s in planets_radiuses.keys():
        print(f"Радіус планети {s} = {planets_radiuses[s]} км")
    else:
        print(f"Вибачте ми не змогли знайти планету {s}")