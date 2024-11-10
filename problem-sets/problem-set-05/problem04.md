## Problem 4

You are given a dataset named `college_football/cfb.csv` summarizing the past ten years of college football games.
The *columns* of the dataset are described in the first line of the file, and each *row* thereafter describes a particular game.

Your task is to analyze one aspect of the fighting Irish's performance by computing the average number of points by which Notre Dame *beat* an opponent in each of the ten years of this data.

Define a function that takes one `str` input `arg1`.

1. `arg1` represents a path to this dataset file.

The function returns a dictionary whose **keys** are integers representing the years in the dataset and whose **values** are the *average number of points* by which Notre Dame *beat* an opposing team in that year.

The file must be located at the relative path `data/college_football/cfb.csv` with respect to the Python file that calls this function.

| **Name:**         | `fighting_irish`                      |
| ----------------- | ------------------------------------- |
| **Inputs:**       | (`str`)                               |
| **Outputs:**      | (`dict[int, float]`)                  |
| **Side Effects:** | None.                                 |
| **Restrictions:** | You *may not* `import` any libraries. |
