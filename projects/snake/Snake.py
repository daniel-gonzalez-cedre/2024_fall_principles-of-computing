from sys import stdout, stderr
from time import sleep
from blessed import Terminal

from Point import Point

# ◀ ▶ ▴ ▾
class Snake:
  def __init__(self, term):
    # term = term if term is not None else Terminal()
    self.body = [Point(term.width//2 - x, term.height//2) for x in range(3)]
    self.face = Point(1, 0)

  @property
  def location(self):
    return self.body[0]

  def __len__(self):
    return len(self.body)

  def __iter__(self):
    return iter(self.body)

  @property
  def head(self):
    return self.body[0]

  @property
  def tail(self):
    return self.body[-1]

  def turn(self, direction: Point):
    assert abs(direction) == 1
    if -self.face != direction:
      self.face = direction

  def move(self, direction: str | Point = ""):
    self.body = [self.head + self.face] + self.body[:-1]

  def grow(self):
    self.body += [self.tail]
