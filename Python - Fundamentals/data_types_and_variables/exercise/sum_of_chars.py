lines = int(input())

sum_chars = 0
for i in range(lines):
    char = input()
    sum_chars += ord(char)
print(f"The sum equals: {sum_chars}")