file = open("mbox.txt", "r")
count = 0
for line in file:
    if line.startswith("From:"):
        print(line.rstrip().split("@")[1])
        count += 1
print("Total", count, "hosts printed")
file.close()
