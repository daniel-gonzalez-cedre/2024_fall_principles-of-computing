## Problem 4

Consider the following hypothetical scheme for determining whether or not one list of integers is *"less than or equal to"* another list of integers: given two lists `list1` and `list2` whose elements are all integers, we say that `list1 <= list2` if and only if (by definition) **any** of the following statements is **true.**

- `list1` is empty.
- for each index `i` of `list1`:
    - the `i`th element of `list1` is less than or equal to the `i`th element of `list2`.

Conversely, we say that `list1 > list2` if and only if (by definition) **all** of the above conditions are **false.**

Define a function that takes as input one list, whose elements are *lists of integers,* and returns a sorted version of that list according to the sheme described above.
Take special care to note that the scheme above may be making *implicit assumptions* about the lengths of `list1` and `list2`.

| **Name:**         | `list_sort`                                                             |
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

As a reminder, `insertion sort` is the sorting algorithm covered in class and it works as follows.
Suppose you have a list `mylist` that you want to sort.
Perform the following process:

- for each element `l` of `mylist`
    + if `result` is empty, append `l` to `result`
    + otherwise, for each element `r` of `result`
        * if `l` is less than `r`, then insert `l` into `result` right before `r`
        * otherwise, if `r` is the last element of `result`, then append `l` to `result`

<details open><summary>Example</summary>

### Example Input & Output

Invoking `list_sort([[1, 2, 3], [4, 5, 6]])` returns `[[1, 2, 3], [4, 5, 6]]`.

Invoking `list_sort([[1], [], [2], [], [-3]])` returns `[[], [], [-3], [1], [2]]`.

Invoking `list_sort([[1, 2, 3], [2], [2, 1, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6]])` returns `[[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [2], [2, 1, 3]]`.

Invoking `list_sort([[4, 2], [2], [2, 1, 3], [4, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 4], [1, 2, 3, 6], [-1, -2, -3, -4], [-1, 10]])` returns
```
[[-1, -2, -3, -4],
 [-1, 10],
 [1, 2, 3, 4],
 [1, 2, 3, 4],
 [1, 2, 3, 5],
 [1, 2, 3, 6],
 [2],
 [2, 1, 3],
 [4, 2],
 [4, 2, 3, 5]]
```

Invoking `list_sort([[1, 2, 4],
                     [1, 2, 3],
                     [1, 2, 6],
                     [1, 2, 3],
                     [1, 2],
                     [1, 4],
                     [1, 3],
                     [1, 2, 3, 4],
                     [1, 2, 3, 5],
                     [1, 2, 3]])` returns
```
[[1, 2],
 [1, 2, 3],
 [1, 2, 3],
 [1, 2, 3],
 [1, 2, 3, 4],
 [1, 2, 3, 5],
 [1, 2, 4],
 [1, 2, 6],
 [1, 3],
 [1, 4]]
```

</details>
