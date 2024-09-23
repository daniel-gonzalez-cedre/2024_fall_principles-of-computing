# problem 01
def hello_world():
  print("Hello, world!")


# problem 02
def greetings():
  your_name = input("Please enter your name: ")
  return your_name


# problem 03
def garble(name):
  if 3 < len(name):
    return name[0] + name[len(name)//2] + name[-1]
  else:
    return "???"


# problem 04
def palindrome(x):
  return x + x[::-1]


# problem 05
def is_palindrome(x):
  return x.lower() == x.lower()[::-1]


# problem 06
def exam_average(exam1, exam2):
  return round((exam1 + exam2)/2, 3)


# problem 07
def ps_average(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9):
  flag = False
  total = 0
  count = 0

  if x0 > 0:
    flag = True
    total = total + x0
    count = count + 1
  if x1 > 0:
    flag = True
    total = total + x1
    count = count + 1
  if x2 > 0:
    flag = True
    total = total + x2
    count = count + 1
  if x3 > 0:
    flag = True
    total = total + x3
    count = count + 1
  if x4 > 0:
    flag = True
    total = total + x4
    count = count + 1
  if x5 > 0:
    flag = True
    total = total + x5
    count = count + 1
  if x6 > 0:
    flag = True
    total = total + x6
    count = count + 1
  if x7 > 0:
    flag = True
    total = total + x7
    count = count + 1
  if x8 > 0:
    flag = True
    total = total + x8
    count = count + 1
  if x9 > 0:
    flag = True
    total = total + x9
    count = count + 1

  if flag:
    average = total / count
    return round(average, 3)
  else:
    return 0.0


# problem08
def score(problem_sets, exams, project):
  return round(0.4*problem_sets + 0.4*exams + 0.2*projects, 3)


# problem09
def grade(grade_points):
  if 92 < grade_points <= 100:
    return "A"
  if 89 < grade_points <= 92:
    return "A-"
  if 86 < grade_points <= 89:
    return "B+"
  if 83 < grade_points <= 86:
    return "B"
  if 79 < grade_points <= 82:
    return "B-"
  if 76 < grade_points <= 79:
    return "C+"
  if 72 < grade_points <= 76:
    return "C"
  if 69 < grade_points <= 72:
    return "C-"
  if 59 < grade_points <= 70:
    return "D"
  if 0  < grade_points <= 59:
    return "F"


# problem10
def report_card(letter_grade):
  print(letter_grade, "lmao")
