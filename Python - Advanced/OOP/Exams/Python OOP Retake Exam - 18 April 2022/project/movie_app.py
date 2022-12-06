from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __check_user(self, username):
        users = [u.username for u in self.users_collection]
        if username in users:
            return True
        return False

    def __get_user(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    @staticmethod
    def __check_owner(user, movie):
        if movie.owner.username == user.username:
            return True
        return False

    def register_user(self, username: str, age: int):
        if self.__check_user(username):
            raise Exception('User already exists!')

        self.users_collection.append(User(username, age))
        return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        if not self.__check_user(username):
            raise Exception('This user does not exist!')

        user = self.__get_user(username)

        if not self.__check_owner(user, movie):
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__get_user(username)
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        if not self.__check_owner(user, movie):
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        for key, value in kwargs.items():
            if hasattr(movie, key):
                setattr(movie, key, value)

        return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):
        user = self.__get_user(username)
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        if not self.__check_owner(user, movie):
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username: str, movie: Movie):
        user = self.__get_user(username)
        if self.__check_owner(user, movie):
            raise Exception(f'{username} is the owner of the movie {movie.title}!')

        if movie in user.movies_liked:
            raise Exception(f'{username} already liked the movie {movie.title}!')

        movie.likes += 1
        user.movies_liked.append(movie)
        return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__get_user(username)
        if movie not in user.movies_liked:
            raise Exception(f'{username} has not liked the movie {movie.title}!')

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        return '\n'.join(m.details() for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)))

    def __str__(self):
        result = []

        if self.users_collection:
            result.append(f"All users: {', '.join(u.username for u in self.users_collection)}")
        else:
            result.append('All users: No users.')
        if self.movies_collection:
            result.append(f"All movies: {', '.join(m.title for m in self.movies_collection)}")
        else:
            result.append('All movies: No movies.')

        return '\n'.join(result)
