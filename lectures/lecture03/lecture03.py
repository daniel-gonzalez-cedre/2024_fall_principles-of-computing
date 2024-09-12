# last class, we learned about:
#   input() : the built-function for receiving information from `stdin`
#   every piece of data is an `object`
#   objects have `types`:
#     the function type
#     str    : the String type, for messages and text
#     int    : the Integer type, for whole numbers
#   type() : the built-in function for figuring out the type of an object
#   String concatenation with +
#   Integer arithmetic with +, -, *

# QUICK RECAP:
# here's a String
mystring = "Hello"

# the len() function produces the length of a String
print(len(mystring))

# remember that Python practices 0-indexing
first = mystring[0]
last = mystring[-1]
last_again = mystring[len(mystring) - 1]

# you can feed multiple strings to the print() function at once
print(first, last, last_again)

# how do we get the middle-character in a String?
middle_index = len(mystring) / 2

# however, this throws an error because index_of_middle is NOT AN INTEGER
print(mystring[middle_index])  # String indexing requires that the index be an `int`

# Python uses the `float` type for decimal numbers
# the division operation `/` ALWAYS returns a float to be safe
# we can TYPE CAST this float to a String using the `int()` function
actual_middle_index = int(middle_index)
print(mystring[actual_middle_index])

# notice that the `int()` function TRUNCATES everything after the decimal when it casts a `float` to an `int`
print(int(1.333))
print(int(-1.333))

# we could use the INTEGER DIVISION operation `//` to accomplish the same thing with less typing
# whereas division a / b ALWAYS returns a `float` even if the result "looks like an integer",
# integer division a // b ALWAYS returns an `int`, even if the result SHOULD be a decimal
# notice that, unlike `int`, this ROUNDS DOWN when it converts
print( 4 // 3 )
print( (-4) // 3 )

# STRING INDEXING lets you obtain specific characters in a String
testing = "0123456789"
print(testing[5])

# STRING SLICING lets you extract entire (monotonically increasing) substrings from a String
begin = 3  # the index from which we start slicing (INCLUSIVE)
end = 7  # the index at which we stop slicing (EXCLUSIVE)
step = 1  # the number of characters to skip over at each step while we travel from `begin` to `end`
substring = testing[begin:end:step]  # this is the general syntax of a String slice
print(substring)

# when we omit some of these values, Python uses reasonable default values
print(testing[3:7:])  # omitting `step` automatically uses a step size of 1
print(testing[:7:])  # omitting `begin` starts us off at the beginning of the String
print(testing[3::])  # omitting `end` takes us until the end of the String
print(testing[::])  # omitting both `begin` and `end` takes the whole string

# the `step` parameter is actually OPTIONAL; most of the time, you can just use one `:` to slice
print(testing[3:7])
print(testing[:7])
print(testing[3:])
print(testing[:])

# use `step` to skip around a string
print(testing[3:7:1])
print(testing[3:7:2])
print(testing[3:7:3])
print(testing[3:7:4])
print(testing[3:7:5])

# you can use a negative step size to travel backwards; this affects the default values of `begin` and `end`
print(testing[7:3:-1])
print(testing[::-1])  # this is a super short and convenient way of REVERSING A STRING

# what about a step size of 0?
print(testing[::0])

# when the `begin` and `end` bounds don't overlap, Python returns the EMPTY STRING
print(testing[7:3])
print(testing[-3:-7])
print(testing[-7:-3:-1])
