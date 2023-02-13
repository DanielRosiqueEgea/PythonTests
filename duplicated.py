import requests
import json

# Step 1: Fetch the playlist data
playlist_id = "PLw-VjHDlEOgt0bWZd8gvwe1QCQm9tKPV7"
API_KEY = "AIzaSyBx4z9mSyeJ_uVArAGdBK-FwJRQotYKlDs"
url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playlist_id}&key={API_KEY}"
response = requests.get(url)

# Step 2: Store the playlist data
songs = []
print(response.json)

# for item in response.json()["items"]:
#     title = item["snippet"]["title"]
#     artist = item["snippet"]["description"].split("by")[-1].strip()
#     songs.append({"title": title, "artist": artist})

# # Step 3: Compare song information
# unique_songs = set()
# duplicates = []
# for song in songs:
#     if (song["title"], song["artist"]) in unique_songs:
#         duplicates.append(song)
#     else:
#         unique_songs.add((song["title"], song["artist"]))

# # Step 4: Output duplicates
# if duplicates:
#     print("Duplicate songs found:")
#     for song in duplicates:
#         print(f"- {song['title']} by {song['artist']}")
# else:
#     print("No duplicate songs found.")
