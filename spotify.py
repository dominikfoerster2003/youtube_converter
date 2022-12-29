import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json

os.environ['SPOTIPY_CLIENT_ID'] = 'ce78bf23cd5e4a12bcc49c47b622e6ff'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'a458dfcadb0d4011ae5e5193c8ccd7d7'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost/'


scopes = ['user-read-private', 'user-read-email', 'playlist-read-private', 'user-library-read']
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))
spotify_user = sp.me()

path = 'C:/Users/foers/Documents/GIT/playlist_transfer_script/'

def user_information():
    with open (path+'spotify_user.json', 'w') as f:
        json.dump(spotify_user, f)
        
def get_user_id():
    with open (path+'spotify_user.json', 'r') as f:
        data = json.load(f)
        user = data['id']
        print(user)
        return user

def get_user_playlists():
    with open (path+'users_playlists.json','w') as f:
        playlists = sp.current_user_playlists()
        json.dump(playlists, f)
    



# print(spotify_user)

#user_playlists = sp.user_playlists(user=user)

user_information()
print(get_user_playlists())
