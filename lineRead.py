file = open("mbox.txt", "r")
count = 0
for line in file:
    line = line.rstrip()
    if line.startswith("From "):
        dataList = line.split()
        print(dataList[1])
        count += 1
print("Total %d lines were printed" % count)