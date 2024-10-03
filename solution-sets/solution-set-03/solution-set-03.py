# problem 01
def sqrt(n):
  for i in range(0, n+2):
    if i*i > n:
      return i - 1


# problem 02
def twosum(nums, target):
  i = 0
  j = len(nums) - 1

  for itr in range(len(nums)):
    if i >= j:
      return []

    s = nums[i] + nums[j]

    if s < target:
      i += 1
    elif s > target:
      j -= 1
    else:
      return [i, j]

  return []


# problem 03
def is_prime(n):
  for i in range(2, n):
    if n%i == 0:
      return False
  return True


# problem 04
def primes(n):
  primelist = []
  for i in range(2, n):
    if is_prime(i):
      primelist += [i]
  return primelist


# problem 05
def merge(xx, yy):
  merged = []

  i = 0
  j = 0

  for itr in range(len(xx) + len(yy)):
    if xx[i] <= yy[j]:
      merged += [xx[i]]
      i += 1
    else:
      merged += [yy[j]]
      j += 1

    if i >= len(xx) or j >= len(yy):
      break

  merged += xx[i:] + yy[j:]  # one of these two is guaranteed to be empty

  return merged


if __name__ == "__main__":

  # problem 01
  print(0, sqrt(0))
  print(1, sqrt(1))
  print(2, sqrt(2))
  print(3, sqrt(3))
  print(4, sqrt(4))
  print(5, sqrt(5))
  print(6, sqrt(6))
  print(7, sqrt(7))
  print(8, sqrt(8))
  print(9, sqrt(9))
  print(10, sqrt(10))
  print(100, sqrt(100))
  print(1000, sqrt(1000))
  print(50000, sqrt(50000))


  # problem 02
  ll = [13, 18, 18, 21, 28, 34, 37, 39, 52, 57, 60, 64, 67, 67, 71, 84, 86, 89, 98, 98]
  for i in range(30, 70):
    res = twosum(ll, i)
    val = [ll[r] for r in res]
    print(i, res, sum(val))


  # problem 03
  print(is_prime(0))
  print(is_prime(1))
  print(is_prime(2))
  print(is_prime(3))
  print(is_prime(4))
  print(is_prime(5))
  print(is_prime(6))
  print(is_prime(7))
  print(is_prime(8))
  print(is_prime(9))


  # problem 04
  print(primes(1000))


  # problem 05
  print(merge([0, 2, 4], [1, 3, 5]))
  print(merge([0, 1, 2], [0, 2, 4, 4, 4]))
  print(merge([0, 2, 4, 6, 8], [1, 2, 3, 4]))
  print(merge([4, 14, 37, 43, 44], [4, 17, 28, 47]))
  print(merge([0, 12, 14, 15, 19, 21, 34, 38, 41, 48], [-4, -2, -2, 0, 1, 4, 5]))
