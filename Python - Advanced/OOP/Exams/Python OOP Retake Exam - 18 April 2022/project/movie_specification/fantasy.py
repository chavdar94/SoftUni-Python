from project.movie_specification.movie import Movie
from project.user import User


class Fantasy(Movie):
    AGE_RESTRICTION = 6

    def __init__(self, title: str, year: int, owner: User, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f'Fantasy - {Movie.details(self)}'

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 6:
            raise ValueError('Fantasy movies must be restricted for audience under 6 years!')
        self.__age_restriction = value
