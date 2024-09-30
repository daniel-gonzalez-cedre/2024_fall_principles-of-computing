def myfunc(x, y, z):
  a = x*(y + z)

  if (a > 4) and (x != 1):
    print("cool")
  else:
    print("not cool")

  return a

print(myfunc("w", 4, 5))  # this throws a TypeError on line 4
print(myfunc(2, 4, 5))  # but this does not throw any errors

# the `type()` function returns the type of a given Python object
print(type(myfunc))
print(type("w"))
print(type(4))
print(type(5))

# the following two expressions evaluate to `bool` objects
# a > 4
# x != 1

# we can verify this as follows
x = 2
a = x*(4 + 5)
print(a > 4, type(a > 4))
print(x != 1, type(x != 1))

# the two Boolean literals
True
False
# the basic Boolean operators
2 == "2"       # equality              binary (between any two objects)
2 != "2"       # inequality            binary (between any two objects)
2 >  4         # greater-than          binary (between two comparable objects)
2 >= 4         # greater-than-or-equal binary (between two comparable objects)
2 <  4         # less-than             binary (between two comparable objects)
2 <= 4         # less-than-or-equal    binary (between two comparable objects)
not True       # negation              unary  (of a bool)
True and False # conjunction           binary (of two bools)
False or True  # disjunction           binary (of two bools)
"a" in "Cafe"  # elementhood           binary (between an object and an iterable)


def first_for_loop(x):
  for char in x:
    print(char)


def reverse_words_failed_attempt(x):
  current_word = "uhhhh"

  for char in x:
    if char == " ":
      pass
    else:
      current_word = current_word + char
      print(current_word)
