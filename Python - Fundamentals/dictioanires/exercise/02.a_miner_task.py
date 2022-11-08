resources = {}
counter = 0
name = None
while True:    
    data = input()
    if data == 'stop':
        break    
    if counter % 2 == 0:
        name = data
        if data not in resources:
            resources[data] = 0
    else:
        value = int(data)
        resources[name] += value
    counter += 1

for key,value in resources.items():
    print(f'{key} -> {value}')
