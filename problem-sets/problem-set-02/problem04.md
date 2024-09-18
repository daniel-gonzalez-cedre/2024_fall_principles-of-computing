## Problem 4

Define a function that takes two strings `arg1` and `arg2` as inputs.
If `arg1` only contains one character, then the function returns a copy of `arg2` with *every occurrence* of `arg1` removed from it.
Otherwise, the program simply returns `arg2`.

You *are not* permitted to use any built-in `str` methods (e.g., you may not use `"my string".index("m")`).
You *are* permitted to use iteration (e.g., `for` loops.)

| **Name:**         | `remove_all`               |
| ----------------- | -------------------------- |
| **Inputs:**       | (`arg1: str`, `arg2: str`) |
| **Outputs:**      | (`str`)                    |
| **Side Effects:** |                            |
| **Restrictions:** | No `str` methods.          |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `remove_all("e", "Carthago delenda est.")` returns the string `"Carthago dlnda st."`.

Invoking `remove_all("et", "Dulce et decorum est,")` returns the string `"Dulce et decorum est,"`.

Invoking `remove_all(" ", "Perfer et obdura, dolor hic tibi proderit olim.")` returns the string `"Perferetobdura,dolorhictibiproderitolim."`.

Invoking `remove_all("z", "Perfer et obdura, dolor hic tibi proderit olim.")` returns the string `"Perfer et obdura, dolor hic tibi proderit olim."`.

</details>
