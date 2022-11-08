def data_type(command, num):
    if command == "int":
        return int(num) * 2
    elif command == "real":
        return f"{(float(num) * 1.5):.2f}"
    elif command == "string":
        return f"${num}$"


type_of_data = input()
number = input()
print(data_type(type_of_data,number))