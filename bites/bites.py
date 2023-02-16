from itertools import permutations
import os
absolute_path = os.path.abspath(__file__)

VALUES = [100, 400, 800, 1400, 1800, 2200, 2600]

def in_list(word, list):
  i = 0
  while i < len(word):
    is_false = True
    for string in list:
      if i < len(word) - 1 and len(string) == 2 and string[0] == word[i] and string[1] == word[i + 1]:
        i += 2
        is_false = False
        list.remove(string)
        break
      elif string == word[i]:
        i += 1
        is_false = False
        list.remove(string)
        break
    if is_false: return False
  return True

def check_word (word, singles, same, oppo):
  for i in range(2**len(oppo)):
    copy = singles.copy()
    copy.extend(same)
    for x in range(len(oppo)):
      copy.append(oppo[x][int((i / (2**x))) % 2])
    if in_list(word, copy):
      return True
  
  return False


#hinting
#h in t i ng
#in


def main():
  # singles = ["m", "b", "o", "y", "v", "a"]
  # horz = ["lo", "te", "ri"]
  # vert = ["es", "nc"]
  singles = ["h", "i", "t"]
  horz = ["ng", "in"]
  vert = []

  all_letters = singles.copy()
  for string in horz:
    for char in string:
      all_letters.append(char)
  for string in vert:
    for char in string:
      all_letters.append(char)
  dict_file = open(os.path.dirname(os.path.dirname(absolute_path)) + "/words.txt")
  dict = []
  while True:
    word = dict_file.readline().strip()
    if not word:
        break
    max_letters = all_letters.copy()
    addable = True
    for letter in word:
      if not letter in max_letters:
        addable = False
        break
      max_letters.remove(letter)
    if addable:
      dict.append(word)
  dict_file.close()


  bites = set()

  for word in dict:
    if check_word(word, singles, horz, vert) or\
      check_word(word, singles, vert, horz):
      bites.add(word)
  print(sorted(list(bites), key=len, reverse=True))
  # print(len(bites))


  other = open(os.path.dirname(absolute_path) + "/test.txt")
  words = other.read().split()
  #print(bites - set(words))
  #print(set(words) - bites)





if __name__ == "__main__":
  main()