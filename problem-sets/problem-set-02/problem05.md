## Problem 5

Define a function that takes one integer argument `arg1`.
The function returns the sum of the even integers between `arg1` and `10000` inclusive.

Recall that `range(a, b)` returns an *iterable list* containing all of the integers between `a` (inclusive) and `b` (exclusive).

You *are not* permitted to use built-in functions or types that we have not yet studied.
You *are not* permitted to use the `%` operator (if you have seen it before in another class).
You *are* permitted to use iteration (e.g., `for` loops.)

| **Name:**         | `even_sum`                                     |
| ----------------- | ------------------------------------------     |
| **Inputs:**       | (`arg1: int`)                                  |
| **Outputs:**      | (`int`)                                        |
| **Side Effects:** |                                                |
| **Restrictions:** | No built-in functions we have not yet studied. |
|                   | No built-in types we have not yet studied.     |
|                   | No use of % operator.                          |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `even_sum(0)` returns `25005000`.

Invoking `even_sum(10)` returns `25004980`.

Invoking `even_sum(5827)` returns `16516518`.

Invoking `even_sum(-256)` returns `24988488`.

Invoking `even_sum(9999)` returns `10000`.

</details>
