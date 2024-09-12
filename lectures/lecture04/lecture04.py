def get_first_name():
  full_name = input("Enter your full legal name here: ")
  modified_name = full_name + " "

  index_of_space = modified_name.index(" ")

  first_name = full_name[0:index_of_space]
  return first_name


def get_username(x):
  print("Hello, " + x + ".")
  y = input("Please enter your desired username: ")
  z = y.lower()
  return z


def get_password():
  y1 = input("Please enter your password: ")
  y2 = input("Confirm your password: ")

  if y1 == y2:
    if len(y1) < 8:
      1/0
    else:
      return y1
  else:
    1/0


def test_login(x, y):
  print("Simulating login procedure.")
  uname = input("Username: ")
  passwd = input("Password: ")

  if uname.lower() == x:
    if passwd == y:
      print("Access granted.")
      return True

  print("Access denied.")
  return False


def login_setup():
  first_name = get_first_name()

  username = get_username(first_name)
  password = get_password()

  test_login(username, password)


login_setup()
