def num_divide3(number):
    count = 0
    for i in range(1, number + 1):
        if(i % 3 == 0):
            count += 1
    return count

while True:
    try:
        number = input("Enter a positive integer : ")
        if number == "done":
            print("Bye!!")
            break
        number = int(number)
        if number <= 0:
            print("please enter a positive number")
        else:
            print("numbers divisible by 3 among numbers from 1 to", str(number), ":", str(num_divide3(number)))
    except:
        print("please enter a postive number")
