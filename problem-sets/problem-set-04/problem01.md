## Problem 1

A Roman numeral is a string comprised of the symbols `I`, `V`, `X`, `L`, `C`, `D`, and `M` representing an integer number.
The values of these symbols is summarized in the following table.

| **Symbol**        | **Value** |
| ----------------- | --------- |
| `I`               | `1`       |
| `V`               | `5`       |
| `X`               | `10`      |
| `L`               | `50`      |
| `C`               | `100`     |
| `D`               | `500`     |
| `M`               | `1000`    |

The symbols are typically written in decreasing order in terms of value, and the same symbol can appear consecutively up to three times in a row.

For example, the Roman numeral `II` represents the number `2` because `I + I = 1 + 1 = 2`.
Similarly, `XXVII` represents the number `27` since `XX + V + II = 20 + 5 + 2 = 27`

However, the number `4` is *not* represented as `IIII` but as `IV` instead.
Whenever a numeral would have to be repeated four times in a row to represent a number, one copy of it is instead placed before the next *higher* numeral.
For example, `IV` represents `4` because `V - I = 5 - 1 = 4`, and `IX` represents `9` because `X - I = 10 - 1 = 9`.
There are three classes of exceptions like these.

1. `IV` represents `4` and `IX` represents `9`.
2. `XL` represents `40` and `XC` represents `90`.
3. `CD` represents `400` and `CM` represents `900`.

Define a function that takes a Roman numeral (given as a string) and returns the integer represented by that Roman numeral.

| **Name:**         | `roman2int`                                                             |
| ----------------- | -----------                                                             |
| **Inputs:**       | (`arg1: str`)                                                           |
| **Outputs:**      | (`int`)                                                                 |
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

Invoking `roman2int("I")` returns `1`.

Invoking `roman2int("III")` returns `3`.

Invoking `roman2int("XI")` returns `11`.

Invoking `roman2int("CCCXLIX")` returns `349`.

Invoking `roman2int("MMCMXCVI")` returns `2996`.

Invoking `roman2int("MMXXIII")` returns `2023`.

Invoking `roman2int("MMXXIV")` returns `2024`.

</details>
