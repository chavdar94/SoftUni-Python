import re

pattern = r'(@#+)(?P<item>[A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1})(@#+)'
number_group = r'(\d+)'

number_of_barcodes = int(input())

for barcode in range(number_of_barcodes):
    current_barcode = input()
    matches = re.findall(pattern, current_barcode)
    if matches:
        current_group = ''
        n_group = re.findall(number_group, current_barcode)
        if n_group:
            current_group = str(''.join(n_group))
        else:
            current_group = '00'
        print(f'Product group: {current_group}')
    else:
        print('Invalid barcode')
