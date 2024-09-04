# this is a comment: a line that is ignored by Python
# a comment begins with the "#" symbol and extends until the end of the line
# comments may appear on lines by themselves (like these) or appended to the end of lines of code

print("Hello, world!")  # this line sends the message "Hello, world!" to stdout, which displays it to the terminal

print "Hello, world!"  # this line causes a SyntaxError

"Hello, world!"  # this line creates the String "Hello, world!" and does nothing else
                 # a String is created by surrounding a message with "double quotes" or 'single quotes'
                 # although there's no difference between "double" and 'single' quote strings, i suggest "double quotes" because almost every other programming language uses this syntax

Hello, world!  # this line will cause two errors:
               #  1) the ! at the end is a SyntaxError, because that symbol can only be used under special circumstances
               #  2) since these words aren't surrounded by "double quotes," Python will treat them like NAMES
               #     but Python can't find what these names refer to---because they're UNDEFINED---so we get a NameError

print(Hello, world!)  # this line has the same SyntaxError and NameError problems as line 13

# assignment statements have the following syntax:
# name = object
my_message = "Hello, world!"  # this statement gives the string "Hello, world!" the name my_message

# a name is a reference that points to a piece of data
# when Python encounters a defined name, it replaces it by the data it points to
print(my_message)  # as a result, this line writes the message "Hello, world!" to the terminal

print("my_message")  # however, this line writes "my_message" to the terminal
