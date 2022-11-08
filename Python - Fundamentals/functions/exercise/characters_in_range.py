def characters_string(start, end):
    conc_characters = []
    for char in range(ord(start)+1, ord(end)):
        conc_characters.append(chr(char))
    return " ".join(conc_characters)


starting_char = input()
ending_char = input()
print(characters_string(starting_char, ending_char))
