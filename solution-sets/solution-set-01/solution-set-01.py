# problem 01
def hello_world():
  print("Hello, world!")


# problem 02
def greetings():
  your_name = input("Please enter your name: ")
  return your_name


# problem 03
def garble(name):
  if 3 <= len(name):
    return name[0] + name[len(name)//2] + name[-1]
  else:
    return "???"


# problem 04
def palindrome(x):
  return x + x[::-1]


# problem 05
def is_palindrome(x):
  return x == x[::-1]


# problem 06
def exam_average(exam1, exam2):
  return round((exam1 + exam2)/2, 3)


# problem 07
def ps_average(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9):
  total = 0
  count = 0

  if x0 > 0:
    total = total + x0
    count = count + 1
  if x1 > 0:
    total = total + x1
    count = count + 1
  if x2 > 0:
    total = total + x2
    count = count + 1
  if x3 > 0:
    total = total + x3
    count = count + 1
  if x4 > 0:
    total = total + x4
    count = count + 1
  if x5 > 0:
    total = total + x5
    count = count + 1
  if x6 > 0:
    total = total + x6
    count = count + 1
  if x7 > 0:
    total = total + x7
    count = count + 1
  if x8 > 0:
    total = total + x8
    count = count + 1
  if x9 > 0:
    total = total + x9
    count = count + 1

  average = total / count
  return round(average, 3)


# problem08
def score(problem_sets, exams, project):
  return round(0.4*problem_sets + 0.4*exams + 0.2*projects, 3)


# problem09
def grade(grade_points):
  if 93 <= grade_points <= 100:
    return "A"
  if 90 < grade_points <= 93:
    return "A-"
  if 87 < grade_points <= 90:
    return "B+"
  if 83 < grade_points <= 87:
    return "B"
  if 80 < grade_points <= 83:
    return "B-"
  if 77 < grade_points <= 80:
    return "C+"
  if 73 < grade_points <= 77:
    return "C"
  if 70 < grade_points <= 73:
    return "C-"
  if 60 < grade_points <= 70:
    return "D"
  if 0  < grade_points <= 60:
    return "F"


# problem10
def report_card(letter_grade):
  print(letter_grade, "lmao")
