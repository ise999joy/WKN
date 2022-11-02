import os


direc = os.getcwd()


print(direc.split("\\")[-1])

print(direc)


os.rename("start.txt", "fin.txt")

