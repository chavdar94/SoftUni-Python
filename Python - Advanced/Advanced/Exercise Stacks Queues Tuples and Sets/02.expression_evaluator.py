from collections import deque

expression = input().split()

numbers = deque()

for el in expression:
    if el in '+-*/':
        while len(numbers) > 1:
            number_one = numbers.popleft()
            number_two = numbers.popleft()

            if el == '+':
                numbers.appendleft(number_one + number_two)
            elif el == '-':
                numbers.appendleft(number_one - number_two)
            elif el == '/':
                numbers.appendleft(number_one // number_two)
            elif el == '*':
                numbers.appendleft(number_one * number_two)
    else:
        numbers.append(int(el))

print(numbers.popleft())