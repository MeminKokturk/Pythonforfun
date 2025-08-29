import math
import time
i = 2
prime_numbers = []
start_time = time.time()
while i <= 100000:
    n = 2
    indic = True
    while n <= math.sqrt(i):
        rem = i % n
        n += 1
        if rem == 0:
            indic = False
            break
    if indic is True:
        prime_numbers.append(i)
    i += 1
print(prime_numbers)
print("--- %s seconds ---" % (time.time() - start_time))
