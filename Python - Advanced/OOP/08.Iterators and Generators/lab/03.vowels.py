class vowels:
    vowels = 'AEIUYOaeiuyo'

    def __init__(self, text):
        self.text = list(text)
        self.vowels_in_text = [c for c in self.text if c in vowels.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels_in_text:
            raise StopIteration

        return self.vowels_in_text.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
