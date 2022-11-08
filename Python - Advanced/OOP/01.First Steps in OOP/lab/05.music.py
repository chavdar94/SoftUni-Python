class Music:
    def __init__(self, *args):
        self.title = args[0]
        self.artist = args[1]
        self.lyrics = args[2]

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
