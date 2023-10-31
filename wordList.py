file = open("romeo.txt", "r")
all_words = []
for line in file:
    line = line.rstrip()
    wordList = line.split()
    for word in wordList:
        if word not in all_words:
            all_words.append(word)
all_words = sorted(all_words)
print(all_words)