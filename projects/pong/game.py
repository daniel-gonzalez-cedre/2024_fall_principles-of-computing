from sys import stdout, stderr
from time import sleep
from blessed import Terminal

from Point import Point
from utils import write


def draw(term, ball):
  write(term.home + term.clear)

  with term.location(*ball):
    write("■")


def update(term, ball, direction):
  ball += direction

  if ball.x <= 0:
    ball.x *= -1
    direction.x *= -1

  if ball.x > term.width - 1:
    ball.x = 2*(term.width - 1) - ball.x
    direction.x *= -1

  if ball.y <= 0:
    ball.y *= -1
    direction.y *= -1

  if ball.y > term.height - 1:
    ball.y = 2*(term.height - 1) - ball.y
    direction.y *= -1

def game(term, fps: int = 30):
  with term.fullscreen(), term.cbreak(), term.hidden_cursor():
    write(term.home + term.clear)

    ball = Point(term.width//2, term.height//2)
    direction = Point(1, 1)

    with term.location(*ball):
      write("■")

    while True:
      sleep(1/fps)

      update(term, ball, direction)
      draw(term, ball)

  pass


if __name__ == "__main__":
  game(Terminal(), fps=24)
