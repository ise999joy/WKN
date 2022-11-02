
A = set()
for i in range(1, 251):
    A.add(i)


s = int(input("Введіть натуральне число: "))
B = set()


for i in range(1, s + 1):
    
    if s % i == 0:
        B.add(i)


print(A - B)