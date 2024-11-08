## Problem 1

You are given a dataset `baby_names/national_names.csv` summarizing the frequency of occurence of the most popular birth names in the United States by year.
A random subset of the rows in this dataset is given below.

| **ID**         | **name** | **year** | **gender** | **count** |
| -------------- | -------- | -------- | ---------- | --------- |
| 1              | Mary     | 1880     | F          | 7065      |
| 1374           | Hamilton | 1880     | M          | 17        |
| 21076          | Fronia   | 1889     | F          | 9         |
| 1713270        | Zade     | 2011     | M          | 64        |

Your task is to find the most popular name of all time for a given gender.

Define a function that takes two `str` inputs `arg1` and `arg2`.

1. `arg1` represents a path to this dataset file.
2. `arg2` is a character, either `"F"` or `"M"`, representing the gender being queried.

The function must parse the dataset and compute the most popular name out of all names with the gender given by `arg2`.
You should implement this by reading the file line-by-line and creating a dictionary.
The function then returns an ordered pair `(year, name)` corresponding to the most popular name `name` of gender `arg2` in the dataset and the year `year` in which that name occurred as the most popular birth name.

The file must be located at the relative path `data/baby_names/national_names.csv` with respect to the Python file that calls this function.

| **Name:**         | `most_popular_name`                   |
| ----------------- | ------------------------------------- |
| **Inputs:**       | (`arg1: str`, `arg2: str`)            |
| **Outputs:**      | (`tuple[int, str]`)                   |
| **Side Effects:** | None.                                 |
| **Restrictions:** | You *may not* `import` any libraries. |
