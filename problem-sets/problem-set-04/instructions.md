# Problem Set 4

Due date: `11:59pm` on `Thursday, 10th of October, 2024`

## Instructions

For each of the following 5 problems, you will be asked to define a function that takes some **inputs,** produces some **outputs,** and has some number of **side effects.**
Each function must be named according to the problem's instructions.

## Restrictions
**You are not permitted to `import` from any libraries (including built-in libraries).**

You may *only* iterate using `for` loops.
You are free to use `list` comprehensions if you'd like (if you don't know what this means, then ignore this sentence).

The *only* `list` methods you are allowed to use are `list.index()`, `list.append()`, `list.extend()`, `list.pop()`.
- `list.index()` works the same as `str.index()`
- `list.append()` adds a new element to the end of the list
    - example: `[0, 1, 2].append(3)` is the same as `[0, 1, 2] + [3]`
- `list.extend()` is equivalent to concatenation using `+`
    - example: `[0, 1, 2].extend([3, 4])` is the same as `[0, 1, 2] + [3, 4]`
- `list.pop()` removes and returns the last element in the list
    - example: `[0, 1, 2].pop()` returns `2`

You *may* use any `str` method you like.

You *may* use the built-in `sum()`, `max()`, `min()`, and `abs()` functions if you find them convenient.
- `sum([x0, x1, x2, ..., xn])` returns `x0 + x1 + x2 + ... + xn`.
- `max([x0, x1, x2, ..., xn])` returns the *largest* object in the list.
- `min([x0, x1, x2, ..., xn])` returns the *smallest* object in the list.

You *may not* use the built-in `sorted()` function.

<details><summary>Example</summary>

### Example Problem
Suppose you are asked to define a function named `example` that takes two integer inputs, prints their sum to the terminal, and then returns twice that quantity plus `1`.
The instructions for that problem might look something like the following table.

| **Name:**         | `example`                                        |
| ----------------- | ------------------------------------------------ |
| **Inputs:**       | (`arg1: int`, `arg2: int`)                       |
| **Outputs:**      | (`int`)                                          |
| **Side Effects:** | Writes the sum of `arg1` and `arg2` to `stdout`. |
| **Restrictions:** | No `import`, `if`, `for`, `while` statements.    |

This format specifies that:

- the function you define *must* be named `example`.
- the function *requires* two arguments of `int` type (it doesn't matter what they are called).
- the function *returns* one output of `str` type (it doesn't matter what it is called).
- the function *prints* `arg1 + arg2` to `stdout`
- library imports, conditional statements, and iterating loops are prohibitted.

A valid solution might look something like the code below.

```
def example(x, y):
  z = x + y
  print(z)
  return 2*z + 1
```

</details>

<details><summary>Submissions</summary>

### Submitting Your Solution

Your solution should be either a Python file named `ps03_<netid>.py`.
For example, if your NetID is `jdoe3` then your file should be named either `ps03_jdoe3.py`.
Your file should be uploaded directly to Canvas under the assignment created for this problem set.

For the example above, a valid solution could be a file named `ps03_jdoe3.py` containing the following lines of code:
```
def example(x, y):
  z = x + y
  print(z)
  return 2*z + 1
```

</details>
