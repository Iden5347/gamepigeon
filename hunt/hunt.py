import os
import copy as cp
absolute_path = os.path.abspath(__file__)

# f = open("test.txt")
# true_combinations = f.read().split()
# f.close()

DIRECTIONS = [[-1,-1], [-1,0], [-1,1], [0,1], [0,-1], [1,-1], [1,0], [1,1]]

def try_word(word, board):
  for i in range(4):
    for j in range(4):
      copy = cp.deepcopy(board)
      if check_word(word, i, j, copy):
        return True
  return False

def check_word(word, i, j, copy):
  if copy[i][j] == word:
    return True
  
  if copy[i][j] == word[0]:
    copy[i][j] = "_"

    for direction in DIRECTIONS:
      if i + direction[0] >= 0 and i + direction[0] <= 3 and\
        j + direction[1] >= 0 and j + direction[1] <= 3:
        if check_word(word[1:], i + direction[0], j + direction[1], cp.deepcopy(copy)):
          return True
        None
  return False

def main():
  board = [
    "womn",
    "utoe",
    "tsua",
    "wsea"
  ]
  
  dict_file = open(os.path.dirname(os.path.dirname(absolute_path)) + "/words.txt")
  dict = []
  while True:
    word = dict_file.readline().strip()
    if not word:
      break
    possible = True
    board_letters = list("".join(board))
    for letter in word:
      if not letter in board_letters:
        possible = False
        break
      board_letters.remove(letter)
    if possible: dict.append(word)
  
  for i in range(len(board)):
    board[i] = [*board[i]]

  combinations = []
  dict_file.close()
  for word in dict:
    if try_word(word, board) and word not in combinations:
      combinations.append(word)
      
  print(len(combinations))
  combinations = sorted(combinations, key=len, reverse=True)
  for i in range(len(combinations)):
    print(combinations[i])



if __name__ == "__main__":
  main()