class Book:
    def __init__(self, *args):
        self.name = args[0]
        self.author = args[1]
        self.pages = int(args[2])


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
