## Problem 2

Define a function that takes one string input `arg1` and returns the *length of the last word* in `arg1` if `arg1` contains more than one word; otherwise, the function returns `-1`.
The given string will *not* have any leading nor trailing spaces.
A *word* in a string is any (contiguous) substring of maximal length that does not contain a space character.

#### Note:
You *are not* permitted to use iteration (e.g., `for` loops) in your solution to this problem.
You *are* permitted to use the `str` methods we have learned about so far: `str.index()`, `str.lower()`, and `str.upper()`.

| **Name:**         | `len_last_word` |
| ----------------- | --------------- |
| **Inputs:**       | (`arg1: str`)   |
| **Outputs:**      | (`int`)         |
| **Side Effects:** |                 |
| **Restrictions:** | No iteration.   |
|                   | No `str` methods other than `str.index()`, `str.lower()`, `str.upper()` |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `len_last_word("Dulce et decorum est")` returns `3`.

Invoking `len_last_word("tse muroced te ecluD")` returns `5`.

Invoking `len_last_word("1024 = 512 + (256+256)")` returns `9`.

</details>
