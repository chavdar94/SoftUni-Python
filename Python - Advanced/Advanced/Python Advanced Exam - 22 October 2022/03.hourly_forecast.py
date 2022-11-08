def forecast(*args):
    result = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': []
    }
    for location, weather in args:
        result[weather].append(location)

    result_output = []
    for key, value in result.items():
        for val in sorted(value):
            result_output.append(f'{val} - {key}')

    return '\n'.join(result_output)

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
