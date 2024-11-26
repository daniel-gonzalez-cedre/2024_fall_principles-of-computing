from math import sqrt
from sys import stdout, stderr
from time import sleep
from blessed import Terminal

from Point import Point

write = lambda *args, **kwargs: print(*args, **kwargs, end="", flush=True)


if __name__ == "__main__":
  term = Terminal()

  if False:
    write(term.home + term.clear)
    print(term.height, term.width)
    print(f"{term.red}red\n{term.yellow}yellow\n{term.green}green",
          "\nstill green",
          "\nstill green",
          f"\n{term.normal}normal")
    print("normal",
          term.black("black"),
          "normal")
    print(f"{term.blue}{term.bold("bold")}",
          term.italic("italic"),
          term.underline("underlined"),
          term.reverse("reversed"))
    print(f"{term.normal}normal text")
    write(term.home + term.clear)

  if False:
    term.home()
    term.clear()  # clear screen
    term.clear_eol()  # clear forward to end of line
    term.clear_bol()  # clear backward to beginning of line
    term.clear_eos()  # clear forward to end of screen

  if False:
    with term.fullscreen(), term.cbreak():
      print(term.move_y(term.height//2) +
            term.center("press any key"))
      val = term.inkey()
      print(val)

  if False:
    with term.fullscreen(), term.cbreak():
      write(term.home + term.clear)

      val = ""
      while val.lower() != "q":
        val = term.inkey(timeout=1)
        if val == "" or val is None:
          write(".")
        elif val.is_sequence:
          print(f"\ngot sequence: {val.name}, {val.code}")
        else:
          print(f"\ngot: {val}")
      print(term.move_y(term.height//2),
            term.center("goodbye!"),
            term.center("press any key to exit"))
      term.inkey()

  if False:
    with term.fullscreen():
      write(term.move_xy(0, 0))
      write("top")
      with term.location():
        write(term.move_xy(term.width//2, term.height//2))
        write("center")
      write("still at the top")

  if False:
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
      write(term.home + term.clear)

      point = Point(term.width//2, term.height//2)
      write(term.move_xy(*point) + "■")

      direction = Point(1, 1)

      while True:
        sleep(0.1)
        write(term.move_xy(0, 0) + ".")
        write(term.move_xy(term.width, term.height) + ".")

        write(term.move_xy(*point) + " ")
        point += direction

        if point.x <= 0:
          point.x *= -1
          direction.x *= -1

        if point.x > term.width - 1:
          point.x = 2*(term.width - 1) - point.x
          direction.x *= -1

        if point.y <= 0:
          point.y *= -1
          direction.y *= -1

        if point.y > term.height - 1:
          point.y = 2*(term.height - 1) - point.y
          direction.y *= -1

        write(term.move_xy(*point) + "■")

  with term.fullscreen(), term.cbreak():
    write(term.move_xy(term.width//2, 0) + "x")
    sleep(0.5)
    write(term.move_xy(0, 1) + "y")
    sleep(0.5)
    write(term.move_xy(term.width - 1, 2) + "z")
    sleep(2)
