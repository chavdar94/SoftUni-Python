voldemort = False

while True:
    name = input()
    if name == "Welcome!":
        break
    if name == "Voldemort":
        voldemort = True
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

if not voldemort:
    print("Welcome to Hogwarts.")