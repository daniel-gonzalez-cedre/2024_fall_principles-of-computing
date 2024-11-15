
class Snake:
  def __init__(self, species, color="red", length=5):
    self.species = species

    self.color = color
    self.length = length

  def __str__(self):
    # return self.color + str(self.length) + self.species
    title = self.species + "\n"
    head = r"  ____ " + "\n"
    head += r" /. . |" + "\n"
    head += r">---  /" + "\n"
    head += r"  \  / " + "\n"
    head += r"   \ | " + "\n"
    head += r"    \ "

    body = "▐" * self.length

    tail = "0Oo"

    return title + head + body + tail

  def grow(self):
    pass

if __name__ == "__main__":
  snek = Snake("water mocassin", length=5)
  print(snek)

  snek.grow()








  # print("hello world!")
  palette = {
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "black": "\033[90m",
    "clear": "\033[0m"
  }
