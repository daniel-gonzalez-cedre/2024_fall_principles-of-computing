## Problem 2

You are given a dataset `baby_names/state_names.csv` summarizing the frequency of occurence of the most popular birth names in the United States by year.
A random subset of the rows in this dataset is given below.

| **ID**         | **name** | **year** | **gender** | **state** | **count** |
| -------------- | -------- | -------- | ---------- | --------- | --------- |
| 1              | Mary     | 1910     | F          | AK        | 14        |
| 1735867        | Mary     | 1910     | F          | IN        | 619       |
| 4530783        | Jenkins  | 1922     | M          | SC        | 5         |
| 1835606        | Keenan   | 1973     | M          | IN        | 6         |

Your task is, for each gender, to find the state with the most births for that gender in each year.

Define a function that takes two `str` inputs `arg1` and `arg2`.

1. `arg1` represents a path to this dataset file.
2. `arg2` is a character, either `"F"` or `"M"`, representing the gender being queried.

The function must parse the dataset and compute, for each year in the dataset, which state had the most births whose name's gender matches `arg2`.
The function should return a dictionary whose **keys** are the years in the dataset and whose **values** are the associated state names.

The file must be located at the relative path `data/baby_names/state_names.csv` with respect to the Python file that calls this function.

| **Name:**         | `most_popular_state`                  |
| ----------------- | ------------------------------------- |
| **Inputs:**       | (`str`, `str`)                        |
| **Outputs:**      | (`dict[int, str]`)                    |
| **Side Effects:** | None.                                 |
| **Restrictions:** | You *may not* `import` any libraries. |
