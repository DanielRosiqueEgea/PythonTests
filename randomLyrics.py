import lyricsgenius as lg
import os
import random
import re

from genius_config import genius_api_key 
no_special_chars = re.compile(r'[^\w\s_]')
no_parenthesis = re.compile(r'\([^)]*\)')
no_brakets = re.compile(r'\[[^]]*\)')
no_dots = re.compile("^\d+\.\s|\.\w+$")


# genius = lg.Genius(api_key)
genius = lg.Genius(genius_api_key, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
genius.verbose = False
PATH = "E:\\Musikote"



files = os.listdir(PATH)
subdir = os.path.join(PATH, "prueba")
files = files+ os.listdir(subdir)

songs_number = len(files)
# print("HAY ",songs_number," Canciones")
while files:
    
    name = random.choice(files)
    
    # name = files[file]
    files.remove(name)

    refined_name=  re.sub(no_dots, "", name)
    # print(refined_name)
    refined_name = re.sub(no_parenthesis, '', refined_name).strip()
    # refined_name = re.sub(no_brakets, '', refined_name).strip()
    # print(refined_name)
    refined_name = re.sub(no_special_chars, ' ', refined_name)
    # print(refined_name)
    try:
        # print("Buscando: ", refined_name)
        song = genius.search_song(refined_name)
    except Exception as e:
        print("Ha habido un error: ", e)
        break
    if song:
        break
    # os.system('cls' if os.name == 'nt' else 'clear')
  

lyrics = song.lyrics.split("\n")
lyric = ""
while lyric == "":
    lyric =random.choice(lyrics)

print(lyric, "\n--",song.title, " -- ",song.artist)
print("\n ortiginal song: ", name," -> ",refined_name)
# lyrics_split = song.lyrics.split("\n")
# lyric_choice =random.choice(range(1,len(lyrics_split)))
# final_lyric = lyrics_split[lyric_choice]
# print(final_lyric)


