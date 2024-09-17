## Problem 1

Define a function of one string input `arg1` representing a sum or difference of two integers that returns the result of evaluating that operation on *the absolute values* of those integers.

The string will be formatted as follows:

- the string will contain three words
- the first word represents an integer
- the second word will be exactly one symbol, either `+` or `-`, representing addition or subtraction respectively
- the `+`/`-` symbol will be surround by exactly one space character on either side
- the third word represents an integer
- there will be no leading spaces nor trailing spaces in the string

A *word* is defined as any substring that does not contain space white-space characters and is not preceded or succeeded by a non-white-space character.

You *are not* permitted to use iteration (e.g., `for` loops) in your solution to this problem.
You *are* permitted to use the `str` methods we have learned about so far: `str.index()`, `str.lower()`, and `str.upper()`.

| **Name:**         | `add`          |
| ----------------- | -------------- |
| **Inputs:**       | (`arg1: str`)  |
| **Outputs:**      | (`int`)        |
| **Side Effects:** |                |
| **Restrictions:** | No iteration.  |
|                   | No `str` methods other than `str.index()`, `str.lower()`, `str.upper()` |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `add("1 + 2")` returns `3`.

Invoking `add("10 + 10")` returns `20`.

Invoking `add("-10 + 10")` returns `20`.

Invoking `add("-10 - 10")` returns `0`.

Invoking `add("0 - 5")` returns `-5`.

Invoking `add("-0 - -5")` returns `-5`.

</details>
