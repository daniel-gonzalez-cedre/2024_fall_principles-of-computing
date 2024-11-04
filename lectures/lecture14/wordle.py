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

BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# print(BLUE, "hello", RED, "world")
PURPLE = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
CLEAR = "\033[0m"

BLACK = "\033[90m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"

def wordle(word_bank):
  solution = word_bank[randint(0, len(word_bank) - 1)]
  print(solution)

  won = False

  while not won:
    guess = input("Enter your guess here: ")
    message = ""
    score = 0

    if len(guess) == 5:
      # check the solution
      i = 0

      # while i <= 4:
      while i < 5:

        if guess[i] == solution[i]:
          message += (GREEN + guess[i])
          score += 1
        elif guess[i] in solution:
          message += (YELLOW + guess[i])
        else:
          message += (BLACK + guess[i])

        message += CLEAR

        i += 1

      print(message)
      won = (score == 5)

    else:
      # reject
      print(f"hey dummy no, your string {guess} is {len(guess)} chars long, and that's not 5")


wordle(word_bank)
