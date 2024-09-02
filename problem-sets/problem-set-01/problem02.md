## Problem 2

Define a function that prompts the user to enter their name and then returns their name.

| **Name:**         | `greetings`               |
| ----------------- | ------------------------- |
| **Inputs:**       | None.                     |
| **Outputs:**      | (`str`)                   |
| **Side Effects:** | Reads `var1` from `stdin` |
| **Restrictions:** |                           |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `greetings()` prompts the user by sending the following message to `stdout`:
```
What is your name? 
```

Suppose the user enters the following response:
```
What is your name? Duncan Idaho
```

The function then receives `Duncan Idaho` from `stdin` and *returns* the string `"Duncan Idaho"`.
This function does not print anything to `stdout` apart from the initial prompt.

</details>
