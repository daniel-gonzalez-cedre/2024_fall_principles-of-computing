from random import random, randint
from loading import load_word_bank, load_word_dict
from guessing import human_guess

BOLD = "\033[1m"
UNDERLINE = "\033[4m"

PURPLE = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
CLEAR = "\033[0m"

BLACK = "\033[90m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"


def wordle():
  # word_bank = load_word_bank("wordle.csv")
  word_dict = load_word_dict("wordle.csv")

  word_bank = [key for key, value in word_dict.items()]
  word_bank = [key for key in word_dict.keys()]
  # word_bank = [key for key in word_dict.values()]
  word_bank = [key for key in word_dict]

  # solution = word_bank[randint(0, len(word_bank) - 1)]
  solution = word_bank[randint(0, len(word_bank) - 1)]
  print(solution)

  won = False

  while not won:
    # guess = input("Enter your guess here: ")
    guess = human_guess()

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


if __name__ == "__main__":
  wordle()
