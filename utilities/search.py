from utilities.requester import get_data

def search(search_term):
    search_term = search_term.replace(" ", "+")
    url = f"https://api.spotify.com/v1/search?q={search_term}&type=album%2Cartist%2Ctrack"
    json_data = get_data(url)

    return json_data