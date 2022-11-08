def operate(operator, *args):
    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def multiply():
        result = args[0]
        for num in args[1:]:
            result *= num
        return result

    def divide():
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    if operator == '+':
        return add()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
