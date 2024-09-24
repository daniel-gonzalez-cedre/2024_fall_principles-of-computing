# problem 01
def add(computation):
  index = computation.index(" ")

  term1 = int(computation[:index])
  if term1 < 0:
    term1 = -term1

  term2 = int(computation[index + 3:])
  if term2 < 0:
    term2 = -term2

  operation = computation[index + 1]

  if operation == "+":
    return term1 + term2
  else:
    return term1 - term2


# problem 02
def len_last_word(string):
  backwards = string[::-1]
  index = backwards.index(" ")
  return len(backwards[:index])


# problem 03
def remove_first_two(char, string):
  if len(char) == 1 and char in string:
    string = string + char  # ensure string.index() doesn't crash our program

    i = string.index(char)  # first occurence
    j = (i + 1) + string[i + 1:].index(char)  # second occurence

    string = string[:i] + string[i + 1 : j] + string[j + 1 : -1]  # ignore the last char

  return string


# problem 04
def remove_all(char, string):
  result = ""
  for c in string:
    if c != char:
      result = result + c
  return result


# problem 05
def even_sum(n):
  total = 0
  for i in range(n, 10000 + 1):
    if (i/2) == (i//2):  # check that `i` is even
      total = total + i
  return total


if __name__ == "__main__":
  # example 01
  print("Problem 01")
  print("   ", add("1 + 2"))
  print("   ", add("10 + 10"))
  print("   ", add("-10 + 10"))
  print("   ", add("-10 - 10"))
  print("   ", add("0 - 5"))
  print("   ", add("-0 - -5"))

  # example 02
  print("Problem 02")
  print("   ", len_last_word("Dulce et decorum est"))
  print("   ", len_last_word("tse muroced te ecluD"))
  print("   ", len_last_word("1024 = 512 + (256+256)"))

  # example 03
  print("Problem 03")
  print("   ", remove_first_two("e", "Carthago delenda est."))
  print("   ", remove_first_two("et", "Dulce et decorum est"))
  print("   ", remove_first_two(" ", "Perferetobdura, dolor hic tibi proderit olim."))
  print("   ", remove_first_two("z", "Perfer et obdura, dolor hic tibi proderit olim."))

  # example 04
  print("Problem 04")
  print("   ", remove_all("e", "Carthago delenda est."))
  print("   ", remove_all("et", "Dulce et decorum est"))
  print("   ", remove_all(" ", "Perferetobdura, dolor hic tibi proderit olim."))
  print("   ", remove_all("z", "Perfer et obdura, dolor hic tibi proderit olim."))


  # example 05
  print("Problem 05")
  print("   ", even_sum(0))
  print("   ", even_sum(10))
  print("   ", even_sum(5827))
  print("   ", even_sum(-256))
  print("   ", even_sum(9999))
