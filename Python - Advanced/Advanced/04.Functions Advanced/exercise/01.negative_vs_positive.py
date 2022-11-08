def sum_numbers(numbers):
    def negatives():
        return [x for x in numbers if x < 0]

    def positives():
        return [x for x in numbers if x >= 0]

    sum_positives = sum(positives())
    sum_negatives = sum(negatives())

    print(sum_negatives)
    print(sum_positives)

    if sum_positives > abs(sum_negatives):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')


numbers = [int(x) for x in input().split()]
sum_numbers(numbers)
