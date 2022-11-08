from os import walk

result = {}
for _, _, files in walk(''):
    for file in files:
        extension = file.split('.')[-1]
        if extension not in result:
            result[extension] = []
        result[extension].append(file)

with open('report.txt', 'w') as file:
    for key, value in sorted(result.items()):
        file.write('.' + key + '\n')

        for path_file in sorted(value):
            file.write(f'- - - {path_file}\n')
