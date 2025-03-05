import os
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
import dotenv

# date = input("Which your do you want to travel to? format YYYY-MM-DD: ")
date = "2024-07-15"

dotenv.load_dotenv()

try:
    with open("data.txt", "r") as file:
        data = file.read()
    if not data:
        raise FileNotFoundError
except FileNotFoundError:
    data = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
    data.raise_for_status()
    with open("data.txt", "w") as file:
        file.write(data.text)

soup = BeautifulSoup(data, "html.parser")
song_names_spans = soup.select("li.lrv-u-width-100p > ul > li > h3#title-of-a-story")
song_names = [name.text.strip() for name in song_names_spans]


spotipy_client_id = os.environ["SPOTIPY_CLIENT_ID"]
spotipy_client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
spotipy_redirect_uri = os.environ["SPOTIPY_REDIRECT_URI"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotipy_client_id,
                                               client_secret=spotipy_client_secret,
                                               redirect_uri=spotipy_redirect_uri,
                                               show_dialog= True,
                                               cache_path=".cache",
                                               scope="playlist-modify-private",))

user_info = sp.current_user()
# print(f"user id: {user_info['id']}")
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=2)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found")

playlist = sp.user_playlist_create(user=user_info["id"], name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist["id"], items= song_uris)































