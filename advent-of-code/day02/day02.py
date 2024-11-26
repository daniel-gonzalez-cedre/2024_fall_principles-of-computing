def parts():
  with open("./day02.csv", "r") as file:
    cubes = {"red": 12,
             "green": 13,
             "blue": 14}
    games = {}

    for line in file:
      head, body = line.strip().split(":")

      idn = int(head.split(" ")[1].strip())
      games[idn] = {"possible" : True,
                    "red"      : 0,
                    "green"    : 0,
                    "blue"     : 0}

      possible = True

      for game in map(lambda x: x.split(","), body.split(";")):
        for hand in game:
          number, color = hand.strip().split(" ")

          if games[idn]["possible"] and int(number) > cubes[color]:
            games[idn]["possible"] = False

          games[idn][color] = max(games[idn][color], int(number))
      games[idn]["power"] = games[idn]["red"] * games[idn]["blue"] * games[idn]["green"]

  part1 = sum(idn for idn in games if games[idn]["possible"])
  part2 = sum(games[idn]["power"] for idn in games)
  return part1, part2


if __name__ == "__main__":
  print(parts())
