class dictionary_iter:

    def __init__(self, element):
        self.element = list(element.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.element)-1:
            raise StopIteration

        self.index += 1
        return self.element[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
