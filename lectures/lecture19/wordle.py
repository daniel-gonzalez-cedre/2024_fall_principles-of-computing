from random import random, randint
from loading import load_word_list, load_word_dict
from guessing import human_guess, machine_guess

def wordle():
  database = load_word_dict("wordle.csv")
  words = [key for key in database]
  solution = words[randint(0, len(words) - 1)]
  won = False

  print(solution)

  while not won:
    # guess = human_guess()
    guess = machine_guess(database)

    if len(guess) == 5:
      message = ""
      score = 0

      # check the guess
      for i in range(5):
        if guess[i] == solution[i]:
          color = "green"
          score += 1
        elif guess[i] in solution:
          color = "yellow"
        else:
          color = "red"

        message += palette[color] + guess[i] + palette["clear"]

      print(message)
      won = (score == 5)

      if not won:
        del database[guess]

    else:
      print(f"hey dummy no, your string {guess} is {len(guess)} chars long, and that's not 5")


if __name__ == "__main__":
  palette = {
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "black": "\033[90m",
    "clear": "\033[0m"
  }

  wordle()
