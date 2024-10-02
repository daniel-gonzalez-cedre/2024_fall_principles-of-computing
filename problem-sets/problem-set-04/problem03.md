## Problem 3

Consider the following hypothetical scheme for determining whether or not one list of integers is *"less than or equal to"* another list of integers: given two lists `list1` and `list2` whose elements are all integers, we say that `list1 <= list2` if and only if (by definition) **any** of the following statements is **true.**

- `list1` is empty.
- the *average* of `list1` is less than or equal to the *average* of `list2`.

Conversely, we say that `list1 > list2` if and only if (by definition) **all** of the above conditions are **false.** 
Take special care to note that the scheme above may be making *implicit assumptions* about the lengths of `list1` and `list2`.

Define a function that takes as input one list, whose elements are *lists of integers,* and returns a sorted version of that list according to the sheme described above.

| **Name:**         | `mean_sort`                                                             |
| ----------------- | -----------                                                             |
| **Inputs:**       | (`arg1: list[list[int]]`)                                               |
| **Outputs:**      | (`list[list[int]]`)                                                     |
| **Side Effects:** | None.                                                                   |
| **Restrictions:** | You *may not* `import` any libraries.                                   |
|                   | You *must* implement the sorting algorithm *by hand.*                   |
|                   |     `insertion sort` is recommended but not required                    |
|                   | You *may not* use the `sorted()` function nor the `list.sort()` method. |
|                   | You *may* use the `sum()`, `max()` and `min()` functions.               |
|                   | You *may* use any function or method we have learned about:             |
|                   |     `print()`                                                           |
|                   |     `input()`                                                           |
|                   |     `len()`                                                             |
|                   |     `enumerate()`                                                       |
|                   |     `range()`                                                           |
|                   |     `enumerate()`                                                       |
|                   |     `enumerate()`                                                       |
|                   |     `list.append()`                                                     |
|                   |     `list.insert()`                                                     |
|                   |     any `str` method                                                    |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `mean_sort([[1, 2, 3], [4, 5, 6]])` returns `[[1, 2, 3], [4, 5, 6]]`.

Invoking `mean_sort([[1], [], [2], [], [-3]])` returns `[[], [], [-3], [1], [2]]`.

Invoking `mean_sort([[1, 2, 3], [2], [2, 1, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6]])` returns `[[2, 1, 3], [2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6]]`.

Invoking `mean_sort([[4, 2], [2], [2, 1, 3], [4, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 6], [-1, -2, -3, -4], [-1, 10]])` returns `[[-1, -2, -3, -4], [2, 1, 3], [2], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [4, 2], [4, 2, 3, 5], [-1, 10]]`.

</details>
