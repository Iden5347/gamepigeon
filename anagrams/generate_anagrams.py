import os
absolute_path = os.path.abspath(__file__)

dictionary = open(os.path.dirname(os.path.dirname(absolute_path)) + "/words.txt")
words = dictionary.read().split()
dictionary.close()

anagrams = open("six_letter_anagrams.txt", "w")
ordered = []
for word in words:
    if len(word) == 6 and not ''.join(sorted(word)) in ordered:
        ordered.append(''.join(sorted(word)))
for word in ordered:
    anagrams.write(word + "\n")
anagrams.close()