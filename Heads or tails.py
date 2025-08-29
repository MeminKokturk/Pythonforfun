import random


class color:
   green = '\033[92m'
   red = '\033[91m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'


h_or_t = ["heads", "tails"]
num_of_h = 0
num_of_t = 0
i = 1

trial_num = 99

while i <= trial_num:
    rand_choice = random.choice(h_or_t)
    if rand_choice == "heads":
        num_of_h += 1
    elif rand_choice == "tails":
        num_of_t += 1
    i += 1

if num_of_h > num_of_t:
    print("The result is", color.bold + color.green + color.underline + "HEADS" + color.end,  "with", num_of_h, "times occurrence.")
else:
    print("The result is", color.bold + color.red + color.underline + "TAILS" + color.end,  "with", num_of_t, "times occurrence.")
