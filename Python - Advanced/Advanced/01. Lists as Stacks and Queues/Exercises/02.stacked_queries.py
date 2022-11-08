n = int(input())

num_stack = []
for _ in range(n):
    command = input().split()
    if command[0] == '1':
        num_stack.append(command[1])
    elif command[0] == '2':
        if num_stack:
            num_stack.pop()
    elif command[0] == '3':
        if num_stack:
            print(max(num_stack))
    elif command[0] == '4':
        if num_stack:
            print(min(num_stack))

reversed_stack = []
while num_stack:
    reversed_stack.append(str(num_stack.pop()))
print(', '.join(reversed_stack))