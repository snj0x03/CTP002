def computepay(hours, rate):
    if hours > 40:
        Pay = (40 * rate) + (1.5 * (hours - 40) * rate)
    else:   
        Pay = hours * rate
    return Pay 

try:
    Hours = int(input("Enter Hours : "))
    Rate = int(input("Enter Rate : "))
    print("Pay :", computepay(Hours, Rate))
except:
    print("Error, please enter numeric input")
