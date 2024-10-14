def roman2int(roman):
  integer = 0
  skip = False

  for index, char in enumerate(roman):
    if skip:
      skip = False
    else:
      if 0 <= index + 1 < len(roman):
        next_char =  roman[index + 1]
      else:
        next_char = ""

      if char == "I":
        if next_char == "V":
          integer += 4
          skip = True
        elif next_char == "X":
          integer += 9
          skip = True
        else:
          integer += 1
      elif char == "V":
        integer += 5
      elif char == "X":
        if next_char == "L":
          integer += 40
          skip = True
        elif next_char == "C":
          integer += 90
          skip = True
        else:
          integer += 10
      elif char == "L":
        integer += 50
      elif char == "C":
        if next_char == "D":
          integer += 400
          skip = True
        elif next_char == "M":
          integer += 900
          skip = True
        else:
          integer += 100
      elif char == "D":
        integer += 500
      elif char == "M":
        integer += 1000
      else:
        print("uh oh")
  return integer


def insertion_sort(ll, compare):
  rr = []
  for i, l in enumerate(ll):
    if len(rr) == 0:
      rr.append(l)
      continue

    for j, r in enumerate(rr):
      if compare(l, r):
        rr.insert(j, l)
        break
      elif j == len(rr) - 1:
        rr.append(l)
        break

  return rr


def one_sort(lists):
  def compare_one(list1, list2):
    if len(list1) == 0:
      return True
    return (len(list1) == 0) or ((len(list2) != 0) and list1[0] <= list2[0])

  return insertion_sort(lists, compare_one)


def mean_sort(lists):
  def compare_mean(list1, list2):
    return (len(list1) == 0) or ((len(list2) != 0) and ((sum(list1)/len(list1)) <= (sum(list2)/len(list2))))

  return insertion_sort(lists, compare_mean)


def list_sort(lists):
  def compare_list(list1, list2):
    if len(list1) == 0:
      return True

    for index in range(len(list1)):
      if index >= len(list2):
        return False

      if list1[index] == list2[index]:
        continue
      else:
        return list1[index] < list2[index]

    return True

  return insertion_sort(lists, compare_list)


def roman_sort(romans):
  def compare_roman(roman1, roman2):
    return roman2int(roman1) <= roman2int(roman2)

  return insertion_sort(romans, compare_roman)


if __name__ == "__main__":
  print(roman2int("I"))
  print(roman2int("III"))
  print(roman2int("XI"))
  print(roman2int("CCCXLIX"))
  print(roman2int("MMCMXCVI"))
  print(roman2int("MMXXIII"))
  print(roman2int("MMXXIV"))

  print(one_sort([[1, 2, 3], [4, 5, 6]]))
  print(one_sort([[1], [], [2], [], [-3]]))
  print(one_sort([[1, 2, 3], [2], [2, 1, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6]]))
  print(one_sort([[4, 2], [2], [2, 1, 3], [4, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 6], [-1, -2, -3, -4], [-1, 10]]))

  print(mean_sort([[1, 2, 3], [4, 5, 6]]))
  print(mean_sort([[1], [], [2], [], [-3]]))
  print(mean_sort([[1, 2, 3], [2], [2, 1, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6]]))
  print(mean_sort([[4, 2], [2], [2, 1, 3], [4, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 6], [-1, -2, -3, -4], [-1, 10]]))

  print(list_sort([[1, 2, 3], [4, 5, 6]]))
  print(list_sort([[1, 2, 4],
                   [1, 2, 3],
                   [1, 2, 6],
                   [1, 2, 3],
                   [1, 2],
                   [1, 4],
                   [1, 3],
                   [1, 2, 3, 4],
                   [1, 2, 3, 5],
                   [1, 2, 3]]))
  print(list_sort([[1], [], [2], [], [-3]]))
  print(list_sort([[1, 2, 3], [2], [2, 1, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6]]))
  print(list_sort([[4, 2], [2], [2, 1, 3], [4, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 6], [-1, -2, -3, -4], [-1, 10]]))

  print(roman_sort(["X", "IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]))
  print(roman_sort(["XX", "XIII", "LXXX", "C", "XXVII", "LXXXIII", "XCIII", "VI", "XLIX", "CDXCIX"]))
  print(roman_sort(["CCXXI", "DXXXVI", "DCCXIV", "CCLXXXI", "XXI", "CCV", "MMMMMCMXCIV"]))
