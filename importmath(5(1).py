import math
x = float(input("x:"))
if x>=6:
    y=((3**x-4)+math.log(x)+math.log10(x))
elif -1<x and x<6:
    y=(x**2 + math.sin(2*x))
else:
    y=(2+(2.7*(x**2)))
print(y)