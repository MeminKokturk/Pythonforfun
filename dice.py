import random


class color:
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'


die_one = random.randint(1, 6)
die_two = random.randint(1, 6)
total = die_one + die_two

print("First die is:", color.bold + color.red + str(die_one) + color.end)
print("Second die is:", color.bold + color.green + str(die_two) + color.end)
print("The total is:", color.bold + color.yellow + str(total) + color.end)
