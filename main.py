import youtube_dl
import json

url = 'https://www.youtube.com/watch?v=goH3nPt-50E&list=PLKbcR_4SPW4G_3iEyCygaubDQ_teN0Y9U'

with youtube_dl.YoutubeDL({'format':'m4a'}) as ydl:
    info = ydl.extract_info(url, download=False)
    try:
        info.get