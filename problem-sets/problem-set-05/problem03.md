## Problem 3

You are given a dataset `bible/kjv.csv` containing the full text of the King James Version of the Holy Bible.
A random subset of the rows in this dataset is given below.

| **ID**         | **book** | **chapter** | **verse**  | **text**                                                                                                                                         |
| -------------- | -------- | ----------- | ---------- | ---------------------------------------------------------                                                                                        |
| 1001001        | 1        | 1           | 1          | In the beginning God created the heaven and the earth.                                                                                           |
| 1001002        | 1        | 1           | 2          | "And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters." |
| 2030011        | 2        | 30          | 11         | "And the LORD spake unto Moses, saying,"                                                                                                         |
| 66022021       | 66       | 22          | 21         | The grace of our Lord Jesus Christ be with you all. Amen.                                                                                        |

Your task is to analyze word drift across the books of the Bible.
Parse this corpus into books and, for each book, count the number of times each of the words `God`, `LORD`, and `Jesus Christ` are used (case-agnostic).

Define a function that takes one `str` input `arg1`.

1. `arg1` represents a path to this dataset file.

The function must parse the dataset and compute, for each book in the Bible, a dictionary whose **keys** are the words `God`, `LORD`, and `Jesus Christ`, and whose **values** are the respective counts of each word in that book of the Bible.
The function then returns a dictionary whose **keys** are integers representing each of the books and whose **values** are the aforementioned dictionaries.

The file must be located at the relative path `data/bible/kjv.csv` with respect to the Python file that calls this function.

| **Name:**         | `word_drift`                          |
| ----------------- | ------------------------------------- |
| **Inputs:**       | (`str`)                               |
| **Outputs:**      | (`dict[int, dict[str, int]]`)         |
| **Side Effects:** | None.                                 |
| **Restrictions:** | You *may not* `import` any libraries. |
