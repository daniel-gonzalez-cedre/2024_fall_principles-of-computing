## Problem 5

You are given a dataset named `college_football/cfb.csv` summarizing the past ten years of college football games.
The *columns* of the dataset are described in the first line of the file, and each *row* thereafter describes a particular game.

Your task is to find each conference's *underdog champion* for each of the ten football seasons.
We will define an **underdog** for a particular football game as a team whose win probability was less than their opponent's but who ended up winning the game.
The **underdog champion** for a conference in a particular season is the team in that conference who was underdog most often throughout that season.
Ties should be broken in favor of whichever team provided the most *overall excitement* for the crowd that season (this *must* be implemented, whether there actually are ties to break or not).

Define a function that takes one `str` input `arg1`.

1. `arg1` represents a path to this dataset file.

The function returns a dictionary whose **keys** are integers representing the years in the dataset and whose **values** are dictionaries that map each conference to its respective underdog champion for that year.

The file must be located at the relative path `data/college_football/cfb.csv` with respect to the Python file that calls this function.

| **Name:**         | `most_exciting_conference`            |
| ----------------- | ------------------------------------- |
| **Inputs:**       | (`arg1: str`)                         |
| **Outputs:**      | (`dict[int, dict[str, str]]`)         |
| **Side Effects:** | None.                                 |
| **Restrictions:** | You *may not* `import` any libraries. |
