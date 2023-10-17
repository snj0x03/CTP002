fileName = input("Enter a file name : ")
try:
    file = open(fileName, "r")
except:
    print("File cannot be opened :", fileName)
else:
    for line in file:
        upperLine = line.rstrip().upper()
        print(upperLine)
    file.close()

