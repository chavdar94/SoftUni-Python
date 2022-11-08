coffees = 0

while True:
    event = input()
    if event == "END":
        break

    if event.isupper():
        if event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
            coffees += 2
    elif event.islower():
        if event == "coding" or event == "dog" or event == "cat" or event == "movie":
            coffees += 1


if coffees > 5:
    print("You need extra sleep")
else:
    print(f"{coffees}")