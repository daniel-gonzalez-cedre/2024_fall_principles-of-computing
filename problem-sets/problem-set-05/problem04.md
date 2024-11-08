## Problem 4

You are given a two datasets named `college_football/cfb_2022.csv` and `college_football/cfb_2023.csv` summarizing various statistics about the college football teams playing during the `2022` and `2023` seasons respectively.
The columns of the dataset are described in the first line of each file.

Your task is to analyze one aspect of the fighting Irish's performance by computing the average number of points by which Notre Dame *beat* an opponent in `2022` and comparing that to the same statistic computed for `2023`.

Define a function that no inputs and returns a dictionary whose **keys** are integers representing the years `2022` and `2023` and whose **values** are the average number of points by which Notre Dame *beat* an opposing team in that year.

The two files must be located within the directory at relative path `data/college_football` with respect to the Python file that calls this function.

| **Name:**         | `fighting_irish`                      |
| ----------------- | ------------------------------------- |
| **Inputs:**       | ()                                    |
| **Outputs:**      | (`dict[int, float]`)                  |
| **Side Effects:** | None.                                 |
| **Restrictions:** | You *may not* `import` any libraries. |
