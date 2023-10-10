while True:
    try:
        output_string = ""
        input_string = input("Please enter string : ")

        if input_string == "done":
            print("Bye!")
            break

        for char in input_string:
            if char in ",.:!?":
                continue
            output_string += char.upper()

        print(output_string)

    except:
        continue