# if x and y are integers where y ≥ 0,
# then the modulus (x % y) operator returns the remainder of the quotient x/y

# if we let r = x % y where y ≥ 0, then x, y, and r satisfy the following two conditions:
#   x = yq + r
#   0 ≤ r < y

def fizzbuzz(n):
  for i in range(n):
    if i%15 == 0:
      print("FizzBuzz")
    elif i%3 == 0:
      print("Fizz")
    elif i%5 == 0:
      print("Buzz")
    else:
      print(i)


def fizzbuzz_alt(n):
  for i in range(n):
    message = ""

    if i%3 == 0:
      message += "Fizz"

    if i%5 == 0:
      message += "Buzz"

    if message == "":
      print(i)
    else:
      print(message)


# the str.split() and str.join() string methods
# the s.split(c) method returns a list of all of the substrings of `s` that were separated by `c`
# the c.join(s) method does the opposite: given a list of strings `s`, return a new string that is the concatenation of  all of those strings with the separator `c` added between them

def better_rev_words(sentence):
  result = []

  for word in sentence.split(" "):
    result += [word[::-1]]

  return " ".join(result)

print(better_rev_words("I was the shadow of the waxwing slain"))
print(better_rev_words("By the false azure in the windowpane;"))
