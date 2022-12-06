class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    def __str__(self):
        movies_liked = [m.details() for m in self.movies_liked]
        movies_owned = [m.details() for m in self.movies_owned]
        output = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]
        if self.movies_liked:
            output.append('\n'.join(movies_liked))
        else:
            output.append("No movies liked.")

        output.append("Owned movies:")

        if self.movies_owned:
            output.append('\n'.join(movies_owned))
        else:
            output.append("No movies owned.")

        return "\n".join(output)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.strip() == '':
            raise ValueError('Invalid username!')
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError('Users under the age of 6 are not allowed!')
        self.__age = value
