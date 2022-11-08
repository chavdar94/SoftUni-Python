expression = input()

par_stack = []

for index, value in enumerate(expression):
    if value == '(':
        par_stack.append(index)
    elif value == ')':
        start_index = par_stack.pop()
        print(expression[start_index: index+1])
