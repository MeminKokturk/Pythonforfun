intent = input("What do you want to do? (Write e for encryption or d for decryption): ")
message = input("Please enter the secret message: ")
key = input("Please enter the key: ")
new_str = ""

try:
    key = int(key)
    if intent == "e":
        for i in message:
            asci = ord(i) + key
            new_str = new_str + chr(asci)
        print(new_str)
    elif intent == "d":
        for i in message:
            asci = ord(i) - key
            new_str = new_str + chr(asci)
        print(new_str)
    else:
        print("You have entered unknown variable, please restart the program")
except ValueError:
    print("You have entered unknown variable, please restart the program")