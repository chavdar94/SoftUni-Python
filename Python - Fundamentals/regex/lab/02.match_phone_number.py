import re

pattern = r"(\+359[ ]2[ ]\d{3}[ ]\d{4}\b)|(\+359[-]2[-]\d{3}[-]\d{4}\b)"
numbers = input()

matches = re.finditer(pattern, numbers)
valid_numbers = [match.group() for match in matches]
print(', '.join(valid_numbers))

