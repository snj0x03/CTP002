print("Type 'done' will exit the program")
numberList = []
while True:
    try:
        num = input("Please enter an integer : ")
        if num == "done":
            print("-------Bye!!--------")
            break
        num = int(num)
        numberList.append(num)
        print(numberList, end=", ")
        print("average = %.2f" % (sum(numberList)/len(numberList)))
    except:
        continue
    
    