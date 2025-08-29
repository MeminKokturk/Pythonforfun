count = int(input("Please enter the floor count of the pyramid: "))

for i in range(count + 1):
    space = (2 * count) - (2 * (i))
    print(space * " ", end="")
    for num in range(i):
        print(i, end=" ")
    print("\t")
