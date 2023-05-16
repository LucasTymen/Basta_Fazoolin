from datetime import time

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

brunch_menu = Menu('Brunch', brunch_items,1100, 1600)

early_bird_menu = Menu('Early-Bird',early_bird_items,1500, 1800)

dinner_menu = Menu('Dinner',dinner_items, 1700,2300)

kids_menu = Menu("Kids's Menu", kids_items, 1100, 2100)

print(brunch_menu.name)
print(brunch_menu.items)
print(early_bird_menu.name)
print(early_bird_menu.items)
print(dinner_menu.name)
print(dinner_menu.items)
print(kids_menu.name)
print(kids_menu.items)
