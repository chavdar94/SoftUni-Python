factor = int(input())
count = int(input())

multiples = []
for number in range(1,count+1):
    multiples.append(factor * number)
print(multiples)
