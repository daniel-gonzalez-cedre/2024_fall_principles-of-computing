from time import sleep
import asyncio

from blessed import Terminal

from Point import Point
from utils import write


def draw(term):
  with term.location():
    write(term.home + term.clear)

  with term.location(term.width//2, term.height//2):
    draw(key)


def update(term):
  # hmmm
  return


# this processes user input
def poll(term):
  key = term.inkey()

  if key is None or key == "":
    key = ""

  elif key.upper() in ("W", "A", "S", "D", "H", "J", "K", "L"):
    key = key.upper()

  elif key.upper() in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"):
    key = key.upper()

  elif key.upper() in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
    key = key.upper()

  elif key.is_sequence:
    if key.name == "KEY_ESCAPE" or key.code == 361:
      key = "ESCAPE"
    elif key.name == "KEY_LEFT"  or key.code == 260:
      key = "LEFT"
    elif key.name == "KEY_DOWN"  or key.code == 258:
      key = "DOWN"
    elif key.name == "KEY_UP"    or key.code == 259:
      key = "UP"
    elif key.name == "KEY_RIGHT" or key.code == 261:
      key = "RIGHT"
    elif key.name == "KEY_ENTER" or key.code == 343:
      key = "ENTER"
    elif key.name in ("KEY_BACKSPACE", "KEY_DELETE") or key.code in (263, 330):
      key = "BACKSPACE"

  return key


def game(term):
  with term.fullscreen(), term.hidden_cursor(), term.cbreak():
    player = None
    paddle = None
    key = ""

    # main game loop
    while True:
      key = poll(term)  # wait for user input

      with term.location(term.width//2, term.height//2):
        draw(key)


if __name__ == "__main__":
  asyncio.run(game(Terminal()))
