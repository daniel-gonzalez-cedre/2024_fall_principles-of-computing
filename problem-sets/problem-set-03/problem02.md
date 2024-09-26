## Problem 2

Define a function that takes two inputs: a list of integers `nums` **sorted from least to greatest,** and a non-negative integer `n`.
If there exist two numbers `x` and `y` in `nums` such that `x + y = n` and the indices of `x` and `y` in `nums` are different, then return a list containing the indices of `x` and `y`.
Otherwise, return the empty list.

- You may look at each element in `nums` *at most once.*
- You may return the indices of `x` and `y` in any order if they exist.
- The elements of `nums` will all be non-negative integers.
- The elements of `nums` will be sorted from least to greatest.
- There may be duplicate elements in `nums`.

| **Name:**         | `twosum`                                     |
| ----------------- | -------------------------------------------- |
| **Inputs:**       | (`arg1: list[int]`, `arg2: int`)             |
| **Outputs:**      | (`list[int]`)                                |
| **Side Effects:** |                                              |
| **Restrictions:** | You may look at each list element only once. |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `twosum([2, 3, 4], 6)` returns `[0, 2]`.

Invoking `twosum([2, 3, 4], 7)` returns `[1, 2]`.

Invoking `twosum([2, 3], 7)` returns `[]`.

Invoking `twosum([8, 8], 16)` returns `[0, 1]`.

Invoking `twosum([13, 18, 18, 21, 28, 34, 37, 39, 52, 57, 60, 64, 67, 67, 71, 84, 86, 89, 98, 98], 67)` returns `[4, 7]`.

</details>
