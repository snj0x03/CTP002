input_string = input("Please enter string : ")

Upper, Lower, Number, Other = 0, 0, 0, 0

for char in input_string:
    if char.isupper() == True:
        Upper += 1
    elif char.islower() == True:
        Lower += 1
    elif char.isdigit() == True:
        Number += 1
    else:
        Other += 1

print("Uppercase letters : %d" % Upper)
print("Lowercase letters : %d" % Lower)
print("Numbers : %d" % Number)
print("Other characters : %d" % Other)
    