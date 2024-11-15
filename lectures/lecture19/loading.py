def load_word_list(filename):
  word_bank = []

  with open(filename, "r") as file:
    next(file)

    for line in file:
      processed = line.strip().split(",")

      if processed[-1] != "":
        word_bank.append(processed[0])

  return word_bank


def load_word_dict(filename):
  word_dict = {}

  with open(filename, "r") as file:
    next(file)

    for line in file:
      word, freq, day = line.strip().split(",")

      if day != "":
        word_dict[word] = float(freq)

  return word_dict


if __name__ == "__main__":
  # print(load_word_bank("wordle.csv"))
  print(load_word_dict("wordle.csv"))
