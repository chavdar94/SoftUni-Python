text = input().upper()
new_text = ''
current_text = ''
repetitions = ''
for index in range(len(text)):
    if not text[index].isdigit():
        current_text += text[index]
    else:
        for digit in range(index,len(text)):
            if not text[digit].isdigit():
                break
            repetitions += text[digit]
        repetitions = int(repetitions)
        new_text += current_text * repetitions
        current_text = ''
        repetitions = ''

print(f"Unique symbols used: {len(set(new_text))}")
print(new_text)
