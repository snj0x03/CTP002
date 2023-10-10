while True:
    try:
        input_string = input("Enter two words : ")

        if input_string == "done" or input_string.strip() == "":
            print("Bye!")
            break

        words = input_string.split()

        if len(words) == 2:
            if words[1] > words[0]:
                print(words[0], "comes first")
            else:
                print(words[1], "comes fist")
    except: 
        continue
