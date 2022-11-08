def add_songs(*args):
    result = {}
    output = ''

    for song_name, lyrics in args:
        if song_name not in result:
            result[song_name] = []
        result[song_name].extend(lyrics)

    for name, lyric in result.items():
        output += f'- {name}\n' + '\n'.join(lyric)
        if lyric:
            output += '\n'
    return output


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
