input_string = input("Enter string : ")
print("Input string =", input_string)

for letter in input_string[-1::-1]:
    print(letter)