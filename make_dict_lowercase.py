#makes everything lowercase

dict = open("hunt/test.txt", "r")
words = dict.read().split()
dict.close()
dict = open("hunt/test.txt", "w")
dict.truncate(0)
for word in words:
    dict.write(word.lower() + "\n")
dict.close()