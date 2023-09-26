try:
    Score = int(input("Enter Score : "))
    if Score >= 90 and Score <= 100:
        print("Grade is A")
    elif Score >= 80 and Score < 90:
        print("Grade is B")
    elif Score >= 70 and Score < 90:
        print("Grade is C")
    elif Score >= 60 and Score < 70:
        print("Grade is D")
    elif Score >= 0 and Score < 60:
        print("Grade is F")
    else:
        print("Error, please enter numeric input between 0 and 100")
except:
    print("Error, please enter numeric input between 0 and 100")