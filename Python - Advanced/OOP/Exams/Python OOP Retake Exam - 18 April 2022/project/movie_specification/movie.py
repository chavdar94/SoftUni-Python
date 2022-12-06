from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    def details(self):
        return f'Title:{self.title},' \
               f' Year:{self.year},' \
               f' Age restriction:{self.age_restriction},' \
               f' Likes:{self.likes},' \
               f' Owned by:{self.owner.username}'

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value.strip() == '':
            raise ValueError('The title cannot be empty string!')
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError('Movies weren\'t made before 1888!')
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if type(value) is not User:
            raise ValueError('The owner must be an object of type User!')
        self.__owner = value
