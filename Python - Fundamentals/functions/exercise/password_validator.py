def password_validator(password):
    length = False
    has_digits = False
    has_letters = False
    is_valid = False

    numbers_in_password = 0
    if 6 <= len(password) <= 10:
        length = True
    for i in password:
        if i.isdigit():
            numbers_in_password += 1
    if numbers_in_password >= 2:
        has_digits = True
    if password.isalnum():
        has_letters = True
    if length and has_digits and has_letters:
        is_valid = True
    if is_valid:
        print("Password is valid")
    else:
        if not length:
            print("Password must be between 6 and 10 characters")
        if not has_letters:
            print("Password must consist only of letters and digits")
        if not has_digits:
            print("Password must have at least 2 digits")


user_password = input()
password_validator(user_password)
