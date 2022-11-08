def odd_even_sum(num):
    evens = [int(i) for i in num if int(i) % 2 == 0]
    odds = [int(i) for i in num if int(i) % 2 != 0]
    evens_sum = sum(evens)
    odds_sum = sum(odds)
    return f"Odd sum = {odds_sum}, Even sum = {evens_sum}"


number = input()
print(odd_even_sum(number))