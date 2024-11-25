from sys import stdout, stderr
from time import sleep
from random import random, randint, choice
import asyncio

from blessed import Terminal

from utils import write
from Point import Point
from Snake import Snake


def create_food(term, snake):
  board = [(x, y) for x in range(term.width) for y in range(term.height) if (x, y) not in snake.body]
  cell = choice(board)
  return Point(*cell)


async def poll(term, fps: int = 24):
  return term.inkey(timeout=1/fps)


async def draw(term, snake, food, fps: int = 24, tick: int = 0, clock: int = 1):
  await asyncio.sleep(1/fps)

  if tick % clock == 0:
    with term.location():
      write(term.home + term.clear)

      write(term.red(f"{term.move_xy(*food)}⊙"))

      for segment in snake:
        write(term.green(f"{term.move_xy(*segment)}■"))


async def update(term, snake, food, key, fps: int = 24, tick: int = 0, clock: int = 1):
  if tick % clock != 0:
    return food, -1

  code = -1
  direction = snake.face

  if key is None or key == "":
    pass

  elif key.lower() in ("w", "a", "s", "d", "h", "j", "k", "l"):
    with term.location(0, 0):
      write("hi")

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

  # snake.turn(direction)
  snake.move()

  if snake.location == food:
    snake.grow()
    food = create_food(term, snake)

  return food, code


async def game(term, fps: int = 24, clock: int = 1):
  tick = 1

  with term.fullscreen(), term.cbreak(), term.hidden_cursor():
    write(term.home + term.clear)

    snake = Snake(term)
    for segment in snake:
      write(f"{term.green}{term.move_xy(*segment)}■{term.normal}")

    food = Point(term.width//2 + 10, term.height//2)
    # food = create_food(term, snake)
    write(f"{term.red}{term.move_xy(*food)}⊙{term.normal}")

    key = ""
    dead = False

    while not dead and key is not None:
      polling = asyncio.create_task(poll(term, fps=fps))
      updating = asyncio.create_task(update(term, snake, food, key, fps=fps, tick=tick, clock=clock))
      drawing = asyncio.create_task(draw(term, snake, food, fps=fps, tick=tick, clock=clock))

      key = await polling
      food, state = await updating
      await drawing

      with term.location(0, 0):
        write(key)

      tick = (tick + 1) % clock


if __name__ == "__main__":
  asyncio.run(game(Terminal(), fps=24, clock=1))
