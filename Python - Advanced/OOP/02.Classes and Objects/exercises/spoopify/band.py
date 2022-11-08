from album import Album
from song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name in [a.username for a in self.albums]:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        for alb in self.albums:
            if alb.username in [a.username for a in self.albums] and alb.published:
                return 'Album has been published. It cannot be removed.'
        if album_name in [a.username for a in self.albums]:
            return f'Album {album_name} has been removed.'
        elif album_name not in [a.username for a in self.albums]:
            return f'Album {album_name} is not found.'

    def details(self):
        result = [f'Band {self.name}']
        for band_info in self.albums:
            result.append(band_info.details())
        return '\n'.join(result)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
