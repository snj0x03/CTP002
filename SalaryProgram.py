try:
    Hours = int(input("Enter Hours : "))
    Rate = int(input("Enter Rate : "))
    if Hours > 40:
        Salary = (40 * Rate) + (1.5 * (Hours - 40) * Rate)
    else:   
        Salary = Hours * Rate
    print("Pay :", Salary)
except:
    print("Error, please enter numeric input")
