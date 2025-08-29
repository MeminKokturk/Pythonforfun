inp = input("Please enter a sentence: ")
letter = input("Please enter the letter to be counted: ")

a=0
list = []
countlist = []
for i in inp:
    list.append(i)
    if i == letter:
        countlist.append(int(list.index(i,a))+1)
    a+=1
print(countlist)

print("Your sentence includes", len(countlist) , letter, "letters on", countlist, "th residues")
