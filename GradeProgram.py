def Grade(Score):
    if Score >= 90 and Score <= 100:
        return "A"
    elif Score >= 80 and Score < 90:
        return "B"
    elif Score >= 70 and Score < 90:
        return "C"
    elif Score >= 60 and Score < 70:
        return "D"
    elif Score >= 0 and Score < 60:
        return "F"
    else:
        return "error"

try:
    Score = int(input("Enter Score : "))
    if Grade(Score) != "error":
        print("Grade is", Grade(Score))
    else:
        print("Error, please enter numeric input between 0 and 100")
except:
    print("Error, please enter numeric input between 0 and 100")