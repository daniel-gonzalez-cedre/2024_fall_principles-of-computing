## Problem 8

Define a function that takes three arguments and returns their weighted average according to the formula given in the syllabus.

- The *first* argument represents average **problem set** points.
- The *second* argument represents average **exam** points.
- The *third* argument represents final **project** points.

All arguments and output should be between `0` and `100`.
Round your result to three decimal places using the `round(_, 3)` function: `round(3.14159, 3)` will return `3.142`.

| **Name:**         | `score`                                       |
| ----------------- | ---------------                               |
| **Inputs:**       | (`arg1: float`, `arg2: float`, `arg3: float`) |
| **Outputs:**      | (`float`)                                     |
| **Side Effects:** |                                               |
| **Restrictions:** | Result must be rounded to `3` decimal places. |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `score(100.0, 25.0, 100.0)` returns `70.0`.

Invoking `score(90.0, 50.0, 75.0)` returns `71.0`.

Invoking `score(80.0, 100.0, 90.0)` returns `90.0`.

</details>
