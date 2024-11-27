# https://blessed.readthedocs.io/en/latest/intro.html
# https://github.com/jquast/blessed?tab=readme-ov-file
# use the `blessed` library instead of the `blessings` library

from blessed import Terminal
from time import sleep  # sleep(n) takes an integer `n` and idles the process for `n` seconds


if __name__ == "__main__":
  term = Terminal()
  # print("hello, world")

  # term.fullscreen() is a context manager implemented by the Terminal class
  # on enter, it overrides the terminal display with a fresh blank window to draw on
  # on leave, it restores the terminal display to what it looked like before this indented block
  with term.fullscreen():

    # term.location(x, y) is a context manager implemented by the Terminal class
    # on enter, it moves the terminal to the (x, y) coordinates specified as arguments
    # on leave, it restores the cursor to where it was before entering this indented block
    with term.location(term.width//2, term.height//2):
      # print takes two optional keyword arguments:
      #   end: this is the string which is appended to the end of the message that `print` displays
      #        default value: "\n"
      #   flush: a boolean value indicating `print` should stop buffer its output
      #          setting this to True will cause `print` to immediately display its output
      #          setting this to False will make `print` buffer messages to stdout line-by-line
      #          default value: False

      # we need to keep term.fullscreen() open long enough to see the messages
      print("hello, world", end="", flush=True)
      sleep(1)

      print("hello, world", end="", flush=True)
      sleep(1)

      print("hello, world")
      sleep(1)

    # https://blessed.readthedocs.io/en/latest/location.html
    # we can also move the cursor explicitly using the following Terminal methods:
    #   term.move_xy(x, y)    : moves the cursor to (x, y)
    #   term.move_up(x, y)    : moves the cursor up one row (decrements row number)
    #   term.move_down(x, y)  : moves the cursor down one row (increments row number)
    #   term.move_left(x, y)  : moves the cursor left one column (decrements col number)
    #   term.move_right(x, y) : moves the cursor right one column (increments col number)
    #   term.center(msg)      : horizontally centers the message `msg` on this row
    # the Terminal attribute term.clear is useful if you are already within term.fullscreen():
    #   term.clear : clears the screen
    #   term.home  : moves cursor to (0, 0); this is a shortcut for term.move_xy(0, 0)
    # due to technicalities of the implementation, all of these require you to PRINT the method/attribute to work
    print(term.clear + term.home)
    print(term.center(f"dimensions of this window: {(term.width, term.height)}"))
    sleep(5)

  # term.hidden_cursor() is a context manager implemented by the Terminal class
  # on enter, the cursor is hidden (meaning: it does not render for display, but still exists)
  # on leave, the cursor is unhidden
  with term.fullscreen(), term.hidden_cursor():
    x = term.width//2
    y = term.height//2

    with term.location(x, y):
      print("■", end="", flush=True)

    while True:
      sleep(1)

      x += 1
      y += 1

      with term.location(x, y):
        print("■", end="", flush=True)


