import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json

path = 'C:/Users/foers/Documents/GIT/playlist_transfer_script/'

scope = "user-library-read"

os.environ['SPOTIPY_CLIENT_ID'] = '0392e685c9424d0ca726b9a23c48bb67'
os.environ['SPOTIPY_CLIENT_SECRET'] = '6ca4601af78947f3b0ca9f871dbd5219'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost/'



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
spotify_user = sp.me()

def user_information():
    with open (path+'spotify_user.json', 'w') as f:
        json.dump(spotify_user, f)
        
def get_user_id():
    with open (path+'spotify_user.json', 'r') as f:
        data = json.load(f)
        user = data['id']
        return user

def get_user_playlists():
    sp.user_playlist(user=get_user_id)



# print(spotify_user)

#user_playlists = sp.user_playlists(user=user)

user_information()
#get_user_playlists()
