old_year = int(input())

new_year = old_year

while True:
    new_year += 1
    if len(set(str(new_year))) == len(str(new_year)):
        print(new_year)
        break

