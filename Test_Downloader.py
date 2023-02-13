import os
from pytube import YouTube, Playlist
from Levenshtein import distance
# import eyeD3 

PATH = "E:\\Musikote"
link = input("Enter the link: ")
playlist = Playlist(link)

download = []

for link in playlist:
    # Step 1: Create an empty list named "download"

    yt = YouTube(link)
    title = yt.title

    # Step 2: Start a loop for each yt video.
    duplicated_title = False
    for item in download:
        if distance(item["title"], title) < 3:
            # Step 3: Check if the yt video title exists on the "download" list using Levenshtein distance < 3

            if item["author"] == yt.author:
                # Step 4: If the title exists, check the author, if they have the same author continue with the next yt video

                
                duplicated_title = True
                break

    if duplicated_title:
        # If the title is a duplicate, continue with the next yt video
        continue

    # Step 5: Add the video to the "download" list
    download.append({"title": title, "author": yt.author})

    # Step 6: Download the video as an MP3 and store its metadata (title, author)
    try:
        ys = yt.streams.filter(only_audio=True, mime_type="audio/webm").first()
    except:
        try: 
            ys = yt.streams.first()
        except:
            continue

    out_file = ys.download(PATH + "\\Prueba")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'

    # Store the metadata (title, author)
    # audio_file = eyeD3.Mp3AudioFile(new_file)
    # audio_file.tag.artist = yt.author
    # audio_file.tag.title = yt.title
    # audio_file.tag.save()
