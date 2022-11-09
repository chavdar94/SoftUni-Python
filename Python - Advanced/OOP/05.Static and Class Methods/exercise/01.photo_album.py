from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_ON_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / PhotoAlbum.MAX_PHOTOS_ON_PAGE))

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f'{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}'
        return 'No more free slots'

    def display(self):
        sep = '-' * 11
        result = [sep]

        for photo in range(len(self.photos)):
            result.append(('[] ' * len(self.photos[photo])).rstrip())
            result.append(sep)

        return '\n'.join(result)
