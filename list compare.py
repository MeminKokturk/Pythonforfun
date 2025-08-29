list_a = [10, 20, 30, 40, 10]
list_b = input("Input a list of numbers separated by comma: ")
user_list = list_b.split(",")

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
isequal = True
for i in range(len(user_list)):
    if list_a[i] == user_list[i]:
        isequal = True
    else:
        isequal = False
        break
if isequal:
    print("The lists are identical")
else:
    print("The lists are different")