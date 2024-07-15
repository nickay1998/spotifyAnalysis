from utilities.requester import get_data

def get_artist(id):
    url = f"https://api.spotify.com/v1/artists/{id}"
    json_data = get_data(url)

    return json_data

class Artist:
    def __init__(self, data):
        self.name = data["name"]
        self.followers = data["followers"]["total"]
        self.genres = data["genres"]
        self.id = data["id"]
        self.images = data["images"]
        self.popularity = data["popularity"]
        self.uri = data["uri"]
        self.url = data["external_urls"]["spotify"]