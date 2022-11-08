def explosion(old_text, new_text):
    strength = 0
    new_text = ''
    for index in range(len(old_text)):
        if strength > 0 and old_text[index] != ">":
            strength -= 1
        elif old_text[index] == ">":
            strength += int(old_text[index + 1])
            new_text += old_text[index]
        else:
            new_text += old_text[index]
    print(new_text)


text = input()
filtered_text = ''
explosion(text, filtered_text)
