## Problem 7

Define a function that takes the average of its ten inputs, but only counts an input towards the average *if it is positive!*
If none of the inputs is positive, then output `0.0`.
The inputs may be `int` or `float` type, but the output must be `float` type.
Round your result to three decimal places using the `round(_, 3)` function: `round(3.14159, 3)` will return `3.142`.

| **Name:**         | `ps_average`                                                                                                                                                                                              |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Inputs:**       | (`arg1: int\|float`, `arg2: int\|float`, `arg3: int\|float`, `arg4: int\|float`, `arg5: int\|float`, `arg6: int\|float`, `arg7: int\|float`, `arg8: int\|float`, `arg9: int\|float`, `arg10: int\|float`) |
| **Outputs:**      | (`float`)                                                                                                                                                                                                 |
| **Side Effects:** |                                                                                                                                                                                                           |
| **Restrictions:** | Result must be rounded to `3` decimal places.                                                                                                                                                             |

<details open><summary>Example</summary>

### Example Input & Output

Invoking `ps_average(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0)` returns `5.5`.

Invoking `ps_average(1.0, 0.0, 3.0, 4.0, 5.0, 0.0, 7.0, 8.0, 9.0, 10.0)` returns `5.875`.

Invoking `ps_average(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)` returns `0.0`.

Invoking `ps_average(-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0, -8.0, -9.0, -10.0)` returns `0.0`.

</details>
