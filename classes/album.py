from classes.artist import Artist, get_artist

class Album:
    def __init__(self, data):
        self.name = data["name"]
        self.release_date = data["release_date"]
        self.id = data["id"]
        self.url = data["external_urls"]["spotify"]
        self.uri = data["uri"]
        self.images = data["images"]
        self.artists = {artist["name"]: Artist(get_artist(artist["id"])) for artist in data["artists"]}
        self.data = data