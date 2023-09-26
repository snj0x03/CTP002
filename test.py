try:
    Hours = int(input("Enter hours : "))
    Rate = int(input("Enter rate : "))
    if Hours > 40:
        Salary = (40 * Rate) + (1.5 * (Hours - 40) * Rate)
    else:   
        Salary = Hours * Rate
    print("Pay :", Salary)
except:
    print("Error, please enter numeric input")

try:
    Score = int(input("Enter Score : "))
    if Score >= 90 and Score <= 100:
        print("Grade is A")
    elif Score >= 80:
        print("Grade is B")
    elif Score >= 70:
        print("Grade is C")
    elif Score >= 60:
        print("Grade is D")
    elif Score >= 0 and Score < 60:
        print("Grade is F")
except:
    print("Error, please enter numeric input")
else:
    print("Error, please enter numeric input")

number = 0
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
        print("Error")
print("Sum of input numbers :", sum)
print("number of input : ", count)
print("Average of input number : ", sum/count)
