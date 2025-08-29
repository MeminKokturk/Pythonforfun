def divbyfive(a):
    if a % 5 == 0:
        return True
    else:
        return False

user_list = input("Please enter a list of numbers separated by comma: ")
user_list = user_list.split(",")
print("\nGiven list is:", user_list)
print("\nThe ones divisible by 5 are:")

for i in user_list:
    if divbyfive(int(i)):
        print(i)
