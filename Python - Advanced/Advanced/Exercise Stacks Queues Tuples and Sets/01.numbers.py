first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    command = input()
    if command == 'Check Subset':
        if first_seq.issuperset(second_seq):
            print('True')
        else:
            print('False')
    command = command.split()
    current_command = command[0]
    if current_command == 'Add':
        if command[1] == 'First':
            for num in command[2:]:
                first_seq.add(int(num))
        elif command[1] == 'Second':
            for num in command[2:]:
                second_seq.add(int(num))

    elif current_command == 'Remove':
        if command[1] == 'First':
            for num in command[2:]:
                first_seq.discard(int(num))
        elif command[1] == 'Second':
            for num in command[2:]:
                second_seq.discard(int(num))

print(*sorted(first_seq), sep=', ')
print(*sorted(second_seq), sep=', ')
