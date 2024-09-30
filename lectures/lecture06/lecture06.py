def char_sum(number):
  total = 0

  for digit in number:
    # total = total + int(digit)
    total += int(digit)

  return total

print(char_sum("123456789"))


def reverse_words(sentence):
  result = ""
  word = ""

  for char in (sentence + " "):
    if char != " ":
      word = word + char
    else:
      # result = result +  word[::-1] + " "
      result += word[::-1] + " "

  return result[:-1]

print(reverse_words("Hello, how are you doing?"))


def replace_words_first_char(string):
  begin_word = True
  result = ""

  for char in string:
    if char == " ":
      begin_word = True
      result += char
    else:
      if begin_word:
        result += "?"
        begin_word = False
      else:
        result += char

  return result

print(replace_words_first_char("Hello, how are you doing?"))


def even_sum(ll):
  total = 0

  for x in ll:
    if x/2 == x//2:
      total += x

  return total

print(even_sum([1, 2, 3, 5, -6, 2, 8, 5]))


def sum_even_up_to(n):
  even_digits = [0, 2, 4, 6, 8]
  total = 0

  for i in range(0, n):
    last_digit = int(str(i)[-1])
    if last_digit in even_digits:
      total += 1

  return total

print(sum_even_up_to(100))
