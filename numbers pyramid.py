count = int(input("Please enter the floor count of the pyramid: "))

for i in range(count):
    cons = str(i+1)
    archer = ""
    for num in range(i+1):
        archer = " ".join([archer, cons])
    print(archer)
