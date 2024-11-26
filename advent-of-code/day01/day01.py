def part1(digits):
  with open("./day01.csv", "r") as file:
    total = 0
    for line in file:
      precalibration = [char for char in line if char in digits]
      calibration = int(precalibration[0] + precalibration[-1])
      total += calibration

  return total


def check(digits, numbers, mapping, line):
  for d in digits:
    if d in line:
      return d
  for n in numbers:
    if n in line:
      return mapping[n]
  return None


def part2(digits, numbers, mapping):
  with open("./day01.csv", "r") as file:
    total = 0

    for line in file:
      left = 0
      first = None

      while first is None:
        left += 1
        first = check(digits, numbers, mapping, line[:left])

      right = len(line) - 1
      last = None

      while last is None:
        right -= 1
        last = check(digits, numbers, mapping, line[right:])

      calibration = int(first + last)
      total += calibration

  return total


if __name__ == "__main__":
  mapping = {"one"   : "1",
             "two"   : "2",
             "three" : "3",
             "four"  : "4",
             "five"  : "5",
             "six"   : "6",
             "seven" : "7",
             "eight" : "8",
             "nine"  : "9"}

  numbers = set(mapping.keys())
  digits = set(mapping.values())

  print(part1(digits))
  print(part2(digits, numbers, mapping))
