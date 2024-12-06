class ShoppingList:
  def __init__(self, title="shopping list", groceries=None):
    self.title = title
    self.groceries = groceries if groceries is not None else []

  def __len__(self):
    return len(self.groceries)

  def __add__(self, other):
    return ShoppingList(title=f"{self.title} & {other.title}", groceries=self.groceries + other.groceries)

  def __str__(self):
    message = f"{self.title}:\n"
    for item, price in self.groceries:
      message += f"\t${float(price):.2f}:\t{item}\n"
    message += f"\t------\n"
    message += f"\t${self.cost()}"
    return message

  def __eq__(self, other):
    return sum(map(lambda t: t[1], self.groceries)) == sum(map(lambda t: t[1], other.groceries))

  # def __getitem__(self, index):
    # return self.groceries[index]

  # def __setitem__(self, index, value):
    # item, price = value
    # if index < len(self.groceries):
      # self.groceries[index] = (item, price)
    # else:
      # self.add(item, price)

  # def __contains__(self, query):
    # return query in [item for item, price in self.groceries]

  def add(self, item, price):
    assert isinstance(item, str) and isinstance(price, int | float)
    self.groceries.append((item, price))

  def cost(self):
    return sum(map(lambda t: t[1], self.groceries))

if __name__ == "__main__":
  target = ShoppingList(title="target", groceries=[("prosciutto", 5), ("milk", 3), ("eggs", 2)])
  home_depot = ShoppingList(title="home_depot", groceries=[("hammer", 2), ("nails", 1)])
  # print(len(target))
  # print(len(home_depot))
  # print(len((target + home_depot)))

  print(target)
  print(home_depot)
  print(target + home_depot)
  print(target == home_depot)
  exit()

  # home_depot[0] = ("screwdriver", 1)
  # home_depot[2] = ("hammer", 3)

  print(target)

  print(home_depot)

  full = target + home_depot
  print(full)
