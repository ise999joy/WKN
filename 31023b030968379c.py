import math
import abc
x = float(input('введіть значення х: '))
k = float(input('введіть значення k: '))
a = float(input('введіть значення a: '))
b = float(input('введіть значення b: '))
def func(x,a,b,k):
    l = float((6*k**3) - math.sin(a) + (math.cos(b))**2)* math.sqrt(abc(b)) + pow(math.e,(x)) / pow(3*a,(7))
    return(l)
print(func(x,a,b,k))