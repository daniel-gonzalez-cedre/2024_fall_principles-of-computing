## Problem 3

Define a function that takes a string representing a person's name as input.
The function mangles the string by removing everything except for the first, middle, and last characters and returning this new string.
If the name is at most 3 characters long, then the function instead returns the string `"???"`.

| **Name:**         | `garble`      |
| ----------------- | ------------- |
| **Inputs:**       | (`arg1: str`) |
| **Outputs:**      | (`str`)       |
| **Side Effects:** |               |
| **Restrictions:** |               |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `garble("Frodo")` returns the result `"Foo"`.

Invoking `garble("Bilbo Baggins")` returns the result `"BBs"`.

Invoking `garble("Smeagol")` returns the result `"Sal"`.

Invoking `garble("Sam")` returns the result `"???"`.

</details>
