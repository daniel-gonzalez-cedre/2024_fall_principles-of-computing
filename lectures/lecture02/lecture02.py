# last class, we learned how to write a message to the terminal

# as a reminder, functions are things that take input, perform computation, and then produce output
# when you call a function in Python (e.g., print), the inputs and outputs of that function only live within Python
# since the terminal & shell are a different process than Python, they don't have direct access to the inputs and outputs of functions that Python is running
# in order for different processes, like Python and the shell, to communicate with each other, the OS sets up three kinds of "streams:"
  # `stdout`: used by Python to SEND messages TO the shell
  # `stdin`: used by Python to RECEIVE messages FROM the shell
  # `stderr`: used by Python to SEND ERROR messages TO the shell
    # error messages are important, so they get their own dedicated output stream separate from `stdout`

# to WRITE TO the `stdout` stream, Python uses the `print` function
print("Hello, world!")  # this line sends the message "Hello, world!" from Python to `stdout` to be displayed in the shell
                        # we'll call the message that gets sent to `stdout` a "side effect" (more on this in the future)

# this means the `print` function takes one input (within Python) but returns no output (within Python)
# PRINT():
  # inputs: one String
  # outputs: None
  # side effects: writes the input message to `stdout` from Python

# to RECEIVE FROM the `stdin` stream, Python uses the `input` function
input()  # this line prompts the user at the shell for input and then pipes it to Python via the `stdin` stream
         # Python then replaces "input()" by the message the user typed

# we can also add a prompt message that displays to the user along with the input request by feeding a String to input()
input("Please enter your name here: ")  # this line displays "Please enter your name here: " and then waits for user input

# this means the `input` function takes either zero or one input (within Python) and returns one output (within Python)
# INPUT():
  # inputs: None, or one String
  # outputs: one String
  # side effects: if an input String is provided, writes it to `stdout` as a prompt; then, receives a message from `stdin` and outputs it to Python

# if we want to do something with the input the user provides, we have two options:
print(input("Enter a message to be immediately displayed: "))  # we can immediately use the result (e.g., plugging it into the `print` function)
user_message = input("Enter a message to be stored for later: ")  # we can assign a name to the result for later reference and manipulation
print(user_message)  # for example, to print it later

# the `print` and `input` functions are built-in to Python, but we can define our own function using the `def` keyword
def better_print(x):
  print("This is like the print function, but somehow better.")
  print(x)

# the code block above defines a new function with the name `better_print` that takes one input `x`
# we can call the function by using its name and supplying it an input for `x`
better_print("Go Irish!")  # this line calls the `better_print` function with the String "Go Irish!" as its input
                           # the first thing Python does when calling the function is to assign `x = "Go Irish!"`
                           # Python then executes the contents of `better_print` line-by-line

# the `better_print` function above takes one input from Python, but not directly from the user
# if we want to read `stdin` from our function, we should invoke the built-in `input` function and save the result
def prompts_user_and_prints():
  x = input("Tell me something cool: ")
  print(x)

# like before, we run the function by calling its name and using () parentheses around its inputs
# since we defined this function to take no inputs, we don't feed it anything between the () parentheses
prompts_user_and_prints()  # this will display the prompt "Tell me something cool: " and repeat the user's response back

# every object in python has a TYPE associated with it
# `function` is the type for functions
# `str` is the type for Strings
# `int` is the type for Integers (i.e., whole numbers)
def printing_numbers():  # `printing_numbers` is the name of a `function` type object
  print("10")  # "10" is a `str` type object
  print("10 + 10")  # "10 + 10" is also `str`
  print(10)  # 10 is an `int` type object
  print(10 + 10)

printing_numbers()  # notice the difference between "10 + 10" and 10 + 10 

# Python treats Strings, which are meant for messages, differently from Integers, which are meant to represent numerical quantities
# in general, the type of an object is of immediate importance because it affects how Python behaves towards that object

def are_we_doing_addition():
  # what do you expect to be printed?
  string_add = "10" + "10"
  print(string_add)  # "1010"

  # what do you expect to be printed?
  integer_add = 10 + 10
  print(integer_add)  # 20

# notice that the same + operator does DIFFERENT THINGS depending on if its inputs are Strings or Integers
are_we_doing_addition()

# in order to figure out the TYPE of an object, we can use the built-in `type` function
def what_type_are_you():
  print(type("Hello, world!"))
  print(type("10"))
  print(type("10 + 10"))
  print(type("10" + "10"))
  print(type(10))
  print(type(10 + 10))

# try out these examples yourself and watch what happens
# practice printing these results out to the terminal and figure out what their types are
def arithmetic_examples():
  a = 30 + 20  # integer addition
  b = 30 * 20  # integer multiplication
  c = 30 - 20  # integer subtraction
  d = 30 / 20  # integer division...?
  e = "30" + 20  # is this allowed?
  f = "30" + "20"  # what about this?
  g = "30" - "20"  # is this okay?
  h = "30" * "20"  # does this make sense?
  i = "30" / "20"  # what about this?

# if we want to convert an object to a String, we can CAST its type using the `str` function
this_is_a_string = str(10)
this_is_also_a_string = str("hello")

# we can do something similar to TYPE CAST an object to be an Integer
this_is_an_integer = int("10")
this_is_also_an_integer = int(10)

# but we can only TYPE CAST objects when it makes sense to do so
error1 = int("hello")
error2 = int("one")
is_this_an_error = int(30 / 20)  # EXERCISE: what do you think is happening here?

# there are two fundamentally important aspects of a String:
  # how LONG is it?
  # what are its CHARACTERS?

def string_length():
  # the built-in `len` function lets us compute the length of a String
  length_hello = len("hello")  # what type is this?
  print(length_hello)
  print(type(length_hello))

def string_indexing():
  my_string = "Irish by a million"

  # we use [i] notation to retrieve the character at index i
  first_letter = my_string[1]  # is this the first letter?
  print(first_letter)

  # since Python practices zero-indexing, the first letter of a String is at index 0, not at index 1
  actual_first_letter = my_string[0]  # ah, now I see
  print(actual_first_letter)

  # we have a convenient way of getting the LAST letter in a String
  last_letter = my_string[-1]  # negative indices...?
  print(last_letter)  # same as regular non-negative indices, but starting from the end of the String

  # since Python starts indexing from zero, the last letter is at index len(my_string) - 1
  last_letter_again = my_string[len(my_string) - 1]  # notice that we can do arithmetic inside of the [...] brackets
  print(last_letter_again)

  # try these out; what happens?
  a = my_string[len(my_string)]
  b = my_string[len(my_string) - 1]
  c = my_string[-len(my_string)]
  c = my_string[-len(my_string) - 1]
