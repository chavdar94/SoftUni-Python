expression = input()
opening_par = []

parentheses = {
    '(': ')',
    '[': ']',
    '{': '}'
}

balanced = True
for par in expression:
    if par in '([{':
        opening_par.append(par)
    elif not opening_par:
        balanced = False
        break
    else:
        last_opening_par = opening_par.pop()
        if parentheses[last_opening_par] != par:
            balanced = False
            break
    if not balanced:
        break
if not balanced or opening_par:
    print('NO')
else:
    print('YES')
