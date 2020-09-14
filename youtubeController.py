from youtube_search import YoutubeSearch
import webbrowser

class Youtube():
    def __init__(self):
        self.search = None
        self.result = None

        self.baseURL = 'https://www.youtube.com/'

    def search_music(self, name: str) -> list:
        self.result = YoutubeSearch(name, max_results=1).to_dict()[0]['url_suffix']
        self.search = name

        self.play()

    def play(self):
        webbrowser.open(self.baseURL + self.result, new=2)