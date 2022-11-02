from math import sqrt


X = (1, 2, 2)
Y = (2, 2, 1.5)
distances = []


for i in range(len(X) - 1):
    
    for j in range(i + 1, len(X)):
        
        distances.append(round(sqrt((X[j] - X[i]) ** 2 + (Y[i] - Y[j]) ** 2), 4))

print(distances)