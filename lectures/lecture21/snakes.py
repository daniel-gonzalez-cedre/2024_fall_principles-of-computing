from time import sleep

class Snake:
  def __init__(self, species, color="\033[0m", length=5):
    self.species = species

    self.clear = "\033[0m"
    self.color = color
    self.length = length

    self.title = self.species + "\n"
    self.head = r"  ____ " + "\n"
    self.head += r" /. . |" + "\n"
    self.head += r">---  /" + "\n"
    self.head += r"  \  / " + "\n"
    self.head += r"   \ | " + "\n"
    self.head += r"    \ "
    self.body = "▐"
    self.tail = "0Oo"

  def __add__(self, other):
    if isinstance(other, int):
      self.length += other
      return self
    elif isinstance(other, Snake):
      return Snake("hybrid", length=self.length + other.length, color=self.color)
    else:
      return NotImplemented

  def __len__(self) -> int:
    return self.length

  def __str__(self) -> str:
    return self.color + self.species + "\n" + self.head + (self.body*self.length) + self.tail + self.clear

  def __repr__(self) -> str:
    return self.species + "\n" + self.head + (self.body*self.length) + self.tail

  def grow(self):
    # sleep(1)
    # print("sleeping...")
    self.length += 1

if __name__ == "__main__":
  palette = {"red"    : "\033[91m",
             "yellow" : "\033[93m",
             "green"  : "\033[92m",
             "cyan"   : "\033[96m",
             "blue"   : "\033[94m",
             "purple" : "\033[95m",
             "black"  : "\033[90m",
             "clear"  : "\033[0m"}


  snek = Snake("cobra", length=7)
  snakey = Snake("viper", color=palette["purple"], length=30)

  print(snek + snakey)

  # print(type(snek))
  # print(isinstance(5, Snake))
  # print(isinstance(5.0, int))

  # snek.grow()
  # print(len(snek))

  # print(snek + 5)
  # print(snek)


  # print(snek)
  # snek.grow()
  # snek.grow()
  # snek.grow()
  # snek.grow()
  # snek.grow()
  # print(snek)

  # snek.grow()
