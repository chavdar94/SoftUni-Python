country_names = input().split(', ')
capitals = input().split(', ')

countries = {key: value for key, value in zip(country_names, capitals)}
for key, value in countries.items():
    print(f'{key} -> {value}')