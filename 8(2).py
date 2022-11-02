import numpy as np
from array import *
import random

A = array('i', []) 
B = np.zeros((3, 4), dtype=int)

for i in range(0, 12):
    A.append(random.randint(1, 24))

for i in range(3):
    
    for j in range(4):
        
        B[i][j] = A[i * 4 + j]


print(A)
print(B)
