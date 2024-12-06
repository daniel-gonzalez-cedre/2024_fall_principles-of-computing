def recsum(my_list):
  if len(my_list) == 0:
    return 0
  else:
    print(f"{my_list[0]} + recsum({my_list[1:]})")
    return my_list[0] + recsum(my_list[1:])

def recprint(my_list):
  if len(my_list) == 0:
    pass
  else:
    print(my_list[0])
    recprint(my_list[1:])

# x = [1, 3, 4, 5, 7]

# print("final result:", recsum(x))

# recprint(x)

# for elem in x:
  # print(elem)

def factorial(n):
  total = 1
  for i in range(1, n + 1):
    total = total * i
  return total

# print(factorial(5))

def recfactorial(n):
  print(n)
  if n == 0:
    return 1
  else:
    return n * recfactorial(n - 1)

def recfibbonaci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return recfibbonaci(n - 1) + recfibbonaci(n - 2)


def binarysearch(my_list, query):
  if len(my_list) == 0:
    return False

  middle_of_list = my_list[len(my_list)//2]
  if query == middle_of_list:
    return True
  elif query < middle_of_list:
    return binarysearch(my_list[:len(my_list)//2], query)
  elif middle_of_list < query:
    return binarysearch(my_list[len(my_list)//2 + 1:], query)



x = [-1, 1, 2, 3, 5, 6, 6, 7, 8, 10, 12, 13]
query = 3
print(binarysearch(x, query))
print(binarysearch(x, 11))

# print(recfibbonaci(0))
# print(recfibbonaci(1))
# print(recfibbonaci(2))
# print(recfibbonaci(3))
# print(recfibbonaci(8))


# print(recfactorial(5))
