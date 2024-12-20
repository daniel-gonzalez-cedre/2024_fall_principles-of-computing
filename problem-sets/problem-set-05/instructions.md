# Problem Set 5

Due date: `11:59pm` on `Sunday, the 17th of November, 2024`

## Instructions

For each of the following 5 problems, you will be asked to define a function that takes some **inputs,** produces some **outputs,** and has some number of **side effects.**
Each function must be named according to the problem's instructions.

## Restrictions
**You are not permitted to `import` from any libraries (including built-in libraries).**

<details><summary>Example</summary>

### Example Problem
Suppose you are asked to define a function named `example` that takes two integer inputs, prints their sum to the terminal, and then returns twice that quantity plus `1`.
The instructions for that problem might look something like the following table.

| **Name:**         | `example`                                        |
| ----------------- | ------------------------------------------------ |
| **Inputs:**       | (`int`, `int`)                                   |
|                   | Two integers representing [...]                  |
| **Outputs:**      | (`int`)                                          |
|                   | One plus twice the sum of the two arguments.     |
| **Side Effects:** | Writes the sum of the two arguments to `stdout`. |
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

Your solution should be a Python file named `ps03_<netid>.py`.
For example, if your NetID is `jdoe3` then your file should be named `ps03_jdoe3.py`.
Your file should be uploaded directly to Canvas under the assignment created for this problem set.

For the example above, a valid solution could be a file named `ps03_jdoe3.py` containing the following lines of code:

```
def example(x, y):
  z = x + y
  print(z)
  return 2*z + 1
```

</details>
