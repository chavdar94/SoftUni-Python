user_names = input().split(', ')
print([name for name in user_names if name.isalnum() and 3 <= len(name) <= 16])
