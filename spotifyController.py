import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "streaming app-remote-control user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

devices = sp.devices()
device = devices["devices"][0]["id"]

results = sp.next_track(device)