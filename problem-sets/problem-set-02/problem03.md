## Problem 3

Define a function that takes two strings `arg1` and `arg2` as inputs.
If `arg1` only contains one character, then the function returns a copy of `arg2` with *the first two occurrences* of `arg1` removed from it.
Otherwise, the program simply returns `arg2`.

You *are not* permitted to use iteration (e.g., `for` loops) in your solution to this problem.
You *are* permitted to use the `str` methods we have learned about so far: `str.index()`, `str.lower()`, and `str.upper()`.

| **Name:**         | `remove_first_two`         |
| ----------------- | -------------------------- |
| **Inputs:**       | (`arg1: str`, `arg2: str`) |
| **Outputs:**      | (`str`)                    |
| **Side Effects:** |                            |
| **Restrictions:** | No iteration.              |
|                   | No `str` methods other than `str.index()`, `str.lower()`, `str.upper()` |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `remove_first_two("e", "Carthago delenda est.")` returns the string `"Carthago dlnda est."`.

Invoking `remove_first_two("et", "Dulce et decorum est")` returns the string `"Dulce et decorum est"`.

Invoking `remove_first_two(" ", "Perfer et obdura, dolor hic tibi proderit olim.")` returns the string `"Perferetobdura, dolor hic tibi proderit olim."`.

Invoking `remove_first_two("z", "Perfer et obdura, dolor hic tibi proderit olim.")` returns the string `"Perfer et obdura, dolor hic tibi proderit olim."`.

</details>
