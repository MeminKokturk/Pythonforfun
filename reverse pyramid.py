count = int(input("Please enter a number: "))

for i in range(count):
    diff = count - (i + 1)
    print(diff * " ", end="")
    print((i+1)*"*")