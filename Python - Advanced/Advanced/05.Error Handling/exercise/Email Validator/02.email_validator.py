from custum_exceptions import MustContainOnlyOneAtSymbolError, \
    MustContainAtSymbolError, NameTooShortError, InvalidDomainError

valid_domains = {'.com', '.bg', '.org', '.net'}

while True:
    email = input()

    if email.count('@') > 1:
        raise MustContainOnlyOneAtSymbolError('Must contain only one "@" symbol error')

    email_parts = email.split('@')
    if len(email_parts) != 2:
        raise MustContainAtSymbolError('Email must contain @')

    name, domain_name = email_parts
    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    domain = f'.{domain_name.split(".")[-1]}'
    if domain not in valid_domains:
        raise InvalidDomainError(f'Domain must be one of the folowing: {", ".join(valid_domains)}')

    print('Email is valid')