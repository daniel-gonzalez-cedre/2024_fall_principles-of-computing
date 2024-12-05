class OutOfBoundsError(Exception):
  pass


def write(*args, **kwargs):
  print(*args, **kwargs, end="", flush=True)
