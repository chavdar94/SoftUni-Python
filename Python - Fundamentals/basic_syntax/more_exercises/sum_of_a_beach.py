word = input()

word = word.lower()

water = word.count("water")
sand = word.count("sand")
fish = word.count("fish")
sun = word.count("sun")
print(water + sand + fish + sun)