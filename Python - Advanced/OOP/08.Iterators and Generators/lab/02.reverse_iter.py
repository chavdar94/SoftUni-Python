class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable  # self.iterable = list(iterable)
        self.length = len(self.iterable)
        self.counter = self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= 0:
            raise StopIteration

        self.counter -= 1
        return self.iterable[self.counter]

        # if not self.iterable:
        #     raise StopIteration
        #
        # return self.iterable.pop()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
