sum = 0
count = 0
while True:
    try:
        number = input("Enter a number : ")
        if number == "done":
            break
        number = int(number)
        sum += number
        count += 1
    except:
        print("invalid input. enter a number")
print("Sum of input numbers :", sum)
print("number of input : ", count)
print("Average of input number : ", sum / count)