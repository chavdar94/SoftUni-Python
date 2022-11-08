import re

text = input()
cool_threshold = 1
nums = ''.join(x for x in text if x.isdigit())
for num in nums:
    cool_threshold *= int(num)
print(f'Cool threshold: {cool_threshold}')

pattern = r'(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\1'
text = list(re.finditer(pattern, text))
print(f'{len(text)} emojis found in the text. The cool ones are:')

for found_emoji in text:
    if found_emoji['emoji']:
        current_emoji = found_emoji['emoji']

    current_threshold = sum([ord(char) for char in current_emoji])
    if current_threshold > cool_threshold:
        print(found_emoji[0])