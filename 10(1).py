
f = open("story.txt", "r")


string = f.read()
f.close()


words = string.replace("...", "").replace(".", "").replace(";", "").replace("-", "").replace("!", "").replace("?", "").replace(",", "").replace(":", "").replace("\n", " ")


words = words.split(" ")
print("Кількість слів у тексті - " + str(len(words)))


print("Кількість унікальних слів у тексті - " + str(len(set(words))))


sentences = string.replace("...", "&$").replace(".", "&$").replace("!", "&$").replace("?", "&$").split("&$")

print("Кількість речень у тексті - " + str(len(sentences) - 1))

