## Problem 2

We say that a number `n` is *prime* if and only if, by definition:

- `n` is a natural number (i.e., a non-negative integer)
- `n` is greater than `1`
- `n` is only divisible by `1` and `n`

Define a function that decides whether or not a given integer is prime.

| **Name:**         | `is_prime`     |
| ----------------- | -------------- |
| **Inputs:**       | (`arg1: int`)  |
| **Outputs:**      | (`bool`)       |
| **Side Effects:** |                |
| **Restrictions:** |                |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `is_prime(0)` returns `False`.

Invoking `is_prime(1)` returns `False`.

Invoking `is_prime(2)` returns `True`.

Invoking `is_prime(3)` returns `True`.

Invoking `is_prime(4)` returns `False`.

Invoking `is_prime(5)` returns `True`.

Invoking `is_prime(6)` returns `False`.

Invoking `is_prime(7)` returns `True`.

Invoking `is_prime(8)` returns `False`.

Invoking `is_prime(9)` returns `False`.

</details>
