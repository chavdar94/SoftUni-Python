def sequence(num):
    sequence_sum = [1]
    for i in range(1, num):
        if len(sequence_sum) < 3:
            sequence_sum.append(i)
        else:
            sequence_sum.append(sum(sequence_sum[-3:]))
    return " ".join([str(num) for num in sequence_sum])


number = int(input())
print(sequence(number))
