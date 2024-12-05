from math import sqrt


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __iter__(self):
    return iter((self.x, self.y))

  def __eq__(self, point) -> bool:
    if isinstance(point, Point):
      return (self.x == point.x) and (self.y == point.y)
    if isinstance(point, tuple) or isinstance(point, list):
      return (len(point) == 2) and (self.x == point[0]) and (self.y == point[1])

  def __abs__(self) -> int:
    return int(sqrt(self.x**2 + self.y**2))

  def __add__(self, point):
    return Point(self.x + point.x, self.y + point.y)

  def __iadd__(self, point):
    self.x += point.x
    self.y += point.y
    return self

  def __sub__(self, point):
    return Point(self.x - point.x, self.y - point.y)

  def __isub__(self, point):
    self.x -= point.x
    self.y -= point.y
    return self

  def __neg__(self):
    return Point(-self.x, -self.y)

  def __mult__(self, other):
    if isinstance(other, int | float):  # scalar product
      return Point(scalar*self.x, scalar*self.y)
    elif isinstance(other, Point):  # inner product
      return self.x*other.x + self.y*other.y

  def __rmult__(self, other):
    return self*other

  def __imult__(self, scalar):
    self.x *= scalar
    self.y *= scalar
    return self

  def __mod__(self, num):
    if isinstance(num, int):
      return Point(self.x % num, self.y % num)
    elif isinstance(num, tuple):
      return Point(self.x % num[0], self.y % num[1])
    else:
      raise AssertionError

  def __imod__(self, num):
    if isinstance(num, int):
      self.x %= num
      self.y %= num
    elif isinstance(num, tuple):
      self.x %= num[0]
      self.y %= num[1]
    else:
      raise AssertionError
    return self

  def __str__(self):
    return f"({self.x}, {self.y})"

  def __repr__(self):
    return f"({self.x}, {self.y})"
