# import random

from random import random, randint

# file = open("wordle.csv", "r")

# # do something

# file.close()

word_bank = []

with open("wordle.csv", "r") as file:
  first_line = True

  for line in file:
    if first_line:
      first_line = False
      continue
    else:
      processed_line = line.strip().split(",")

      if processed_line[-1] != "":
        word_bank.append(processed_line[0])  # list of strings

# print(word_bank)

# print(word_bank)

def wordle(word_bank):
  solution = word_bank[randint(0, len(word_bank) - 1)]
  print(solution)

  won = False

  while not won:
    guess = input("Enter your guess here: ")
    if solution == guess:
      print("yay")
      return
    else:
      pass


wordle(word_bank)
