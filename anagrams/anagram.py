import sys
import os
absolute_path = os.path.abspath(__file__)

VALUES = [100, 400, 1200, 2000]

def main():
    if len(sys.argv) != 2:
        print("USAGE: python anagram.py ANAGRAM")
        return 1
    dictionary = open(os.path.dirname(os.path.dirname(absolute_path)) + "/words.txt")
    words = dictionary.read().split()
    dictionary.close()

    anagram_word = sys.argv[1]
    anagram = {}
    for i in anagram_word:
        if not i in anagram.keys():
            anagram[i] = 0
        anagram[i] += 1

    variations = []
    for string in words:
        word = {}
        for x in string:
            if not x in word.keys():
                word[x] = 0
            word[x] += 1
        possible = True
        for letter in word:
            if letter not in anagram.keys() or word[letter] > anagram[letter]:
                possible = False
        if possible: variations.append(string)

    score = 0
    total = 0
    for variation in sorted(variations, key=len, reverse=True):
        if len(anagram_word) <= 6: score += VALUES[len(variation) - 3]
        total += 1
        print(variation, len(variation))
    if len(anagram_word) <= 6: print("score:", score)
    print ("number of words:", total)

if __name__ == "__main__":
    main()