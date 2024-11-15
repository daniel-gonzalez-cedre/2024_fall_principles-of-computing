def human_guess():
  return input("Enter your guess here: ")


def machine_guess(db):
  # words = {key: value for key, value in db.items()}
  words = [key for key, value in db.items()]

  notion_of_comparison = lambda a: -db[a]
  sorted_words = sorted(words, key=notion_of_comparison)

  return sorted_words[0]
