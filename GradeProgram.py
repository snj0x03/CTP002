def Grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 90:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    elif score >= 0 and score < 60:
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