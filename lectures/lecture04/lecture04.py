# get the user's first name
def get_first_name():
  full_name = input("Enter your full legal name here: ")  # prompt the user for their full name

  modified_name = full_name + " "  # to avoid edge-cases that would cause the next line to crash

  index_of_space = modified_name.index(" ")  # this line throw an error if `modified_name` does not have any spaces

  first_name = full_name[0:index_of_space]  # slice the full name up to the index of the first space
  return first_name  # output the first name


# get a username (CASE-INSENSITIVE) from the user
def get_username(x):
  print("Hello, " + x + ".")  # greet the user
  y = input("Please enter your desired username: ")  # prompt the user for their username
  z = y.lower()  # force the provided username to lowercase
  return z  # output the lower-cased username


# obtain a password (CASE-SENSITIVE) from the user
# make user confirm their password by entering it twice
# ensure the password is at least 8 characters long
def get_password():
  y1 = input("Please enter your password: ")  # prompt the user for their password
  y2 = input("Confirm your password: ")  # prompt the user to confirm their password

  if y1 == y2:  # check that y1 is EQUAL to y2
    if len(y1) <= 7:  # check that y1 is long enough
      1/0  # CRASH: password is too short
    else:
      return y1  # return the password
  else:
    1/0  # CRASH: passwords do not match


# simulate the login process
def test_login(x, y):
  print("Simulating login procedure.")
  uname = input("Username: ")
  passwd = input("Password: ")

  if uname.lower() == x:  # enure usernames match
    if passwd == y:  # ensure passwords match
      print("Access granted.")

  print("Access denied.")


def login_setup():
  first_name = get_first_name()

  username = get_username(first_name)
  password = get_password()

  test_login(username, password)


login_setup()
