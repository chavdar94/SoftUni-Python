file_location = input().split('\\')
file = file_location[-1]
file_name, extension = file.split('.')
print(f'File name: {file_name}\nFile extension: {extension}')