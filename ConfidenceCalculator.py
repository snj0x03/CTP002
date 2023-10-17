fileName = input("Enter a file name : ")
try:
    file = open(fileName, "r")
except:
    print("File cannot be opened :", fileName)
else:
    count = 0
    sum = 0
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            sum += float(line.rstrip().split()[1])
            count += 1
    if count == 0:
        average = 0
    else:
        average = sum/count
    print("Average spam confidence :", average)
    file.close()