from project.movie_specification.movie import Movie
from project.user import User


class Thriller(Movie):
    AGE_RESTRICTION = 16

    def __init__(self, title: str, year: int, owner: User, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f'Thriller - {Movie.details(self)}'

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError('Thriller movies must be restricted for audience under 16 years!')
        self.__age_restriction = value
