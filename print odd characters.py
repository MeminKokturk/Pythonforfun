input_string = input("Please enter the input that you want to see the odd characters of: ")
for i in input_string:
   ind = input_string.index(i)
   if ind%2 == 0:
       print(i)