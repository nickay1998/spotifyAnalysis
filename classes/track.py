class Track:
    def __init__(self, data):
        self.name = data["name"]
        self.uri = data["uri"]
        self.popularity = data["popularity"]
        self.preview = data["preview_url"]
        self.id = data["id"]
        self.explicit = data["explicit"]
        self.artists = [artist["name"] for artist in data["artists"]]
        self.album = data['album']['name']
        self.duration = data["duration_ms"]
        self.images = data['album']['images']