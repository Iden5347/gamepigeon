from itertools import permutations
import os
absolute_path = os.path.abspath(__file__)

VALUES = [100, 400, 1200, 2000]

dictionary = open(os.path.dirname(os.path.dirname(absolute_path)) + "/words.txt")
words = dictionary.read().split()
dictionary.close()
dict = [[] for _ in range(26 * 26 * 26)]
for string in words:
    if len(string) <= 6 and len(string) >= 3:
        index = (ord(string[0]) - 97) * 26 * 26 + (ord(string[1]) - 97) * 26 + (ord(string[2]) - 97)
        dict[index].append(string)
def test(anagram_word):
    anagram = {}
    for i in anagram_word:
        if not i in anagram.keys():
            anagram[i] = 0
        anagram[i] += 1

    variations = []
    for permutation in list(permutations([5,4,3,2,1,0], 3)) + list(permutations([0,1,2,3,4,5], 3)):
        index = (ord(anagram_word[permutation[0]]) - 97) * 26 * 26 + (ord(anagram_word[permutation[1]]) - 97) * 26 + ord(anagram_word[permutation[2]]) - 97
        for string in dict[index]:
            word = {}

            for x in string:
                if not x in word.keys():
                    word[x] = 0
                word[x] += 1
            
            possible = True
            for letter in word.keys():
                if letter not in anagram.keys() or word[letter] > anagram[letter] or string in variations:
                    possible = False
            if possible: variations.append(string)

    score = 0
    total = 0
    i = 0
    for variation in variations:
        i += 1
        if len(anagram_word) <= 6: score += VALUES[len(variation) - 3]
        total += 1
    return [score, total]

output = open("scores.txt", "w")
anagrams_file = open("six_letter_anagrams.txt", "r")


most_words = [0, ""]
highest_score = [0, ""]
i = 0

for strand in anagrams_file.read().split():
    results = test(strand)
    if results[0] > highest_score[0]:
        highest_score = [results[0], strand]
    if results[1] > most_words[0]:
        most_words = [results[1], strand]
    output.write((str(strand) + " - score: " + str(results[0]) + " " * (10 - len(str(results[0]))) + "total: " + str(results[1]) + "\n"))
    i+= 1
    print(i)
print (most_words)
print (highest_score)

output.close()
anagrams_file.close()