from sys import stdout, stderr
from time import sleep
from random import random, randint, choice
import asyncio

from blessed import Terminal

from Point import Point
from Snake import Snake
from utils import write, OutOfBoundsError


def create_food(term, snake):
  board = [(x, y) for x in range(term.width) for y in range(term.height) if (x, y) not in snake.body]
  cell = choice(board)
  return Point(*cell)


async def poll(term, fps: int = 24):
  return term.inkey(timeout=1/fps)


def draw(term, snake, food, fps: int = 24):
  with term.location():
    write(term.home + term.clear)

    write(term.red(f"{term.move_xy(*food)}*"))

    for segment in snake:
      with term.location(*segment):
        write(term.green(f"■"))  # █


def update(term, snake, food, key, fps: int = 24):
  code = -1
  direction = snake.face

  if key is None or key == "":
    pass

  elif key.lower() in ("w", "a", "s", "d", "h", "j", "k", "l"):

    code = 1

    if key.lower() in ("a", "h"):
      snake.turn(Point(-1, 0))
    elif key.lower() in ("s", "j"):
      snake.turn(Point(0, 1))
    elif key.lower() in ("w", "k"):
      snake.turn(Point(0, -1))
    else:
      snake.turn(Point(1, 0))

  elif key.lower() == "q":
    pass

  elif key.is_sequence:
    if key.name == "KEY_ESCAPE" or key.code == 361:
      pass
    elif key.name == "KEY_LEFT"  or key.code == 260:
      snake.turn(Point(-1, 0))
    elif key.name == "KEY_DOWN"  or key.code == 258:
      snake.turn(Point(0, 1))
    elif key.name == "KEY_UP"    or key.code == 259:
      snake.turn(Point(0, -1))
    elif key.name == "KEY_RIGHT" or key.code == 261:
      snake.turn(Point(1, 0))

  snake.move()

  if snake.location == food:
    snake.grow()
    food = create_food(term, snake)

  return food, code


async def game(term, fps: int = 24):
  with term.fullscreen(), term.cbreak(), term.hidden_cursor():
    snake = Snake(term)
    for segment in snake:
      with term.location(*segment):
        write(term.green(f"■"))  # █

    food = Point(term.width//2 + 10, term.height//2)
    # food = create_food(term, snake)
    with term.location(*food):
      write(term.red(f"*"))

    key = ""
    dead = False

    while not dead and key is not None:
      sleeping = asyncio.create_task(asyncio.sleep(1/fps))
      polling = asyncio.create_task(poll(term, fps=fps))

      await asyncio.gather(polling, sleeping)
      key = polling.result()

      food, state = update(term, snake, food, key, fps=fps)
      draw(term, snake, food, fps=fps)

      with term.location(0, 0):
        write(key)

if __name__ == "__main__":
  asyncio.run(game(Terminal(), fps=12))
