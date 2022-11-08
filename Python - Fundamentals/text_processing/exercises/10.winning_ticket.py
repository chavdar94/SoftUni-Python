def is_winning(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'
    left_side = ticket[:10]
    right_side = ticket[10:]
    winning_symbols = ['@', '#', '$', '^']
    for symbol in winning_symbols:
        for repeat in range(10, 5, -1):
            winning_combination = symbol * repeat
            if winning_combination in left_side and winning_combination in right_side:
                if repeat == 10:
                    return f'ticket "{ticket}" - {repeat}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {repeat}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(is_winning(ticket))