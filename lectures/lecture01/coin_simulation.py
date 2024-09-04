from multiprocessing import Pool

from tqdm import tqdm

import numpy as np
from numpy.random import default_rng


def simulate(args) -> tuple[bool, list[str]]:
  num_coins, num_flips = args
  rng = np.random.default_rng()

  coin = rng.choice(list(range(num_coins)))

  selected: bool = (coin == 0)
  if selected:
    flips = ["H" for _ in range(num_flips)]
  else:
    flips = ["H" if rng.random() <= 0.5 else "T" for _ in range(num_flips)]

  return selected, flips


if __name__ == "__main__":
  N: int = 100000
  num_coins: int = 1000
  num_flips: int = int(input("How many times should we flip in a row? "))

  rng: np.random.Generator = default_rng()

  count_selected = 0
  count_total = 0
  count = 0

  with Pool() as pool:
    results = pool.imap(simulate, tqdm([(num_coins, num_flips) for _ in range(N)]))

    for selected, flips in results:
      if selected:
        count_selected += 1
      if "T" not in flips:
        count_total += 1
      count += 1

  if count_total == 0:
    print("No sequences of all-heads were observed :( try simulating again.")
  else:
    freq_biased = count_selected / count_total
    freq_fair = (count_total - count_selected) / count_total

    print(f"{count_total} out of {N} coin flip sequences landed heads {num_flips} times in a row.")
    print(f"BIASED coin: {count_selected} times \t {100*freq_biased:0.3f}% of the time")
    print(f"FAIR coin:   {count_total - count_selected} times \t {100*freq_fair:0.3f}% of the time")

    print(f"\nIf you see a sequence of {num_flips} heads in a row, ", end="")

    if freq_biased > freq_fair:
      print("you should believe the coin is BIASED.")
    elif freq_biased < freq_fair:
      print("you should believe the coin is FAIR.")
    else:
      print("you can't know whether it's biased or fair.")
