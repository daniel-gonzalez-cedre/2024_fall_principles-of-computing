from sys import stdout, stderr
from time import sleep
from random import random, randint, choice
import asyncio

from blessed import Terminal

from Point import Point
from utils import write


def draw(term, snake, food, fps: int = 24):
  with term.location():
    write(term.home + term.clear)

  with term.location(term.width//2, term.height//2):
    draw(key)


def update(term, snake, food, key, fps: int = 24):
  # hmmm
  return


# this processes user input
async def poll(term, fps: int = 24):
  key = term.inkey(timeout=1/fps)

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


async def game(term, fps: int = 24):
  with term.fullscreen(), term.cbreak(), term.hidden_cursor():
    player = None
    paddle = None
    key = ""

    ball = Ball()
    with term.location(*ball):
      write("■")

    # main game loop
    while True:
      # the next four lines look for user input once per frame
      sleeping = asyncio.create_task(asyncio.sleep(1/fps))
      polling = asyncio.create_task(poll(term, fps=fps))
      await asyncio.gather(polling, sleeping)
      key = polling.result()

      with term.location(term.width//2, term.height//2):
        draw(key)


# modify the framerate by changing `fps`
if __name__ == "__main__":
  asyncio.run(game(Terminal(), fps=24))
