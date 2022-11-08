import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()

valid_names = re.findall(pattern,text)
print(*valid_names)