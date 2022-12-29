import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ['SPOTIPY_CLIENT_ID'] = 'ce78bf23cd5e4a12bcc49c47b622e6ff'
os.environ['SPOTIPY_CLIENT_SECRET'] = '9f5867af20704063869a149e7000de5e'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost/'

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None