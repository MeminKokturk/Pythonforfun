number = input("Please input the number for palindrome check: ")

rev_num = number[::-1]

if int(rev_num) == int(number):
    print("This number is palindromic")
else:
    print("This number is not palindromic")