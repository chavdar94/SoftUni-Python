class Party:
    people = []

    def __init__(self):
        pass


party_people = Party
while True:
    name = input()
    if name == "End":
        break

    party_people.people.append(name)
print(f"Going: {', '.join(party_people.people)}")
print(f"Total: {len(party_people.people)}")