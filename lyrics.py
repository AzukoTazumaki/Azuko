import os

fbn_path = 'static/lyrics/albums/funny_but_nobody/'
fbn_lyrics_paths = [fbn_path + f"{i}" + '.csv' for i in range(4)]
result = {}
for index, lyrics in enumerate(fbn_lyrics_paths):
    result[index] = [x.split('\n') for x in open(os.path.join(lyrics), 'r').read().splitlines()]

print(result)