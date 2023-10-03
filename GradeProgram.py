def Grade(Score):
    if Score >= 90 and Score <= 100:
        return "Grade is A"
    elif Score >= 80 and Score < 90:
        return "Grade is B"
    elif Score >= 70 and Score < 90:
        return "Grade is C"
    elif Score >= 60 and Score < 70:
        return "Grade is D"
    elif Score >= 0 and Score < 60:
        return "Grade is F"
    else:
        return "Error, please enter numeric input between 0 and 100"

try:
    Score = int(input("Enter Score : "))
    print(Grade(Score))
except:
    print("Error, please enter numeric input between 0 and 100")