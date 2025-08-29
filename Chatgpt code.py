import random

def toss_coin():
  # Generate a random number between 0 and 1
  coin = random.randint(0, 1)
  # If the number is 0, return 'heads'
  if coin == 0:
    return 'heads'
  # If the number is 1, return 'tails'
  elif coin == 1:
    return 'tails'

# Toss the coin and print the result
result = toss_coin()
print(f'The coin landed on {result}')
