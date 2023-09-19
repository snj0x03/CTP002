S = int(input("Enter seconds : "))
Hours = S // 3600
Minutes = (S%3600) // 60
Seconds = S % 60
print(str(S), "seconds is", str(Hours), "hours,", str(Minutes), "minutes,", str(Seconds), "seconds")