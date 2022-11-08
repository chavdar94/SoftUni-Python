lines = int(input())

bracket = ")"
is_same = False
for char in range(lines):
    character = input()
    if character == chr(ord(")")) or character == chr(ord("(")):
        if character == bracket:
            print("UNBALANCED")
            is_same = True
            break
        else:
            bracket = character
if not is_same:
    print("BALANCED")


