hours = int(input("Enter Hours : "))
rate = float(input("Enter Rate : "))
print("Salary : " + str(hours*rate))

celsius = float(input("Enter Celsius Temperature : "))
print("Fahrenheit Temperature : " + str(celsius*9/5 + 32))

S = int(input("Enter seconds : "))
Hours = int(S/3600)
Minutes = int((S%3600)/60)
Seconds = S%60
print(str(S), "seconds is", str(Hours), "hours,", str(Minutes), "minutes,", str(Seconds), "seconds")