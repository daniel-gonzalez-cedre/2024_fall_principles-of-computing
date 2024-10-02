## Problem 5

Define a function that takes a list of roman numerals and returns the list sorted in increasing order *according to the numerical value of the roman numerals.*

| **Name:**         | `roman_sort`                                                            |
| ----------------- | ------------                                                            |
| **Inputs:**       | (`arg1: list[str]`)                                                     |
| **Outputs:**      | (`list[str]`)                                                           |
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

Invoking `roman_sort(["X", "IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"])` returns `["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]`.

Invoking `roman_sort(["XX", "XIII", "LXXX", "C", "XXVII", "LXXXIII", "XCIII", "VI", "XLIX", "CDXCIX"])` returns `["VI", "XIII", "XX", "XXVII", "XLIX", "LXXX", "LXXXIII", "XCIII", "C", "CDXCIX"]`.

Invoking `roman_sort(["CCXXI", "DXXXVI", "DCCXIV", "CCLXXXI", "XXI", "CCV", "MMMMMCMXCIV"])` returns `["XXI", "CCV", "CCXXI", "CCLXXXI", "DXXXVI", "DCCXIV", "MMMMMCMXCIV"]`.

</details>
