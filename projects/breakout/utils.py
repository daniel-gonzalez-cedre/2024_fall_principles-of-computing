# write(x) is the same as print(x, end="", flush=True)
# this function is provided for convenience
def write(*args, **kwargs):
  print(*args, **kwargs, end="", flush=True)
