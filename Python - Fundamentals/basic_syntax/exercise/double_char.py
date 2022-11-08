while True:
    data = input()
    if data == "End":
        break
    elif data == "SoftUni":
        pass
    else:
        for char in data:
            print(char * 2, end="")
        print()