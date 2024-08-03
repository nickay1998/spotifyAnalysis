import streamlit as st
import streamlit_antd_components as sac
from classes import Album, Artist, Track
from streamlit_card import card
from utilities.requester import get_data
from pages import show_details

def search(search_term):
    search_term = search_term.replace(" ", "+")
    url = f"https://api.spotify.com/v1/search?q={search_term}&type=album%2Cartist%2Ctrack"
    search_json = get_data(url)

    search_results = {}    

    for search_type in search_json:
        search_results[search_type] = []

        for result in search_json[search_type]["items"]:
            print(f"{search_type}: {result['name']}")

            if search_type == "albums":
                search_results[search_type].append(Album(result))
            elif search_type == "artists":
                search_results[search_type].append(Artist(result))
            elif search_type == "tracks":
                search_results[search_type].append(Track(result))

    return search_results

def add_page(title, data):
    titles = [page.title for page in st.session_state["pages"]]
    existing_ids = [data.id for data in list(st.session_state["page_details"].values())]
    if title in titles and data.id not in existing_ids:
        done = False
        i = 1
        while not done:
            title = f"{title} ({i})"
            if title not in titles:
                done = True
            else:
                i = i + 1
    elif data.id in existing_ids:
        return
    
    st.session_state["page_details"][title] = data
    st.session_state["pages"].append(st.Page(show_details, title=title, url_path=title))
    nav = st.navigation(st.session_state["pages"])

with st.form(key="Search"):
    if "search_text" not in st.session_state:
        search_text = st.text_input("Search")
    else:
        search_text = st.text_input("Search", value=st.session_state["search_text"])
    st.form_submit_button(label="Submit")

if search_text != "":
    if "search_text" in st.session_state:
        if search_text == st.session_state["search_text"]:
            search_raw_results = st.session_state["search_raw_results"]
    else:
        search_raw_results = search(search_text)

    search_types = list(search_raw_results.keys())
    display_type = sac.tabs(search_types, align='center', use_container_width=True)
    columns = int(st.session_state["window_width"] / 270)
    columns = 2 if columns < 2 else columns

    grouped_list = [search_raw_results[display_type][i:i+columns] for i in range(0, len(search_raw_results[display_type]), columns)]

    for group in grouped_list:
        cols = st.columns(columns)
        for i, result in enumerate(group):
            with cols[i]:
                name = result.name

                if len(result.images) > 0:
                    image_link = result.images[0]["url"]
                else:
                    image_link = ""

                card(
                    title="",
                    text=name,
                    image=image_link,
                    styles={
                        "card": {
                            "width": "100%", "height": "width", "border-radius": "10px", "aspect-ratio": "1","box-shadow": "0 0 0px rgba(0,0,0,0.5)", "margin": "1px"
                        },
                        "filter": {
                            "background-color": "rgba(0, 0, 0, 0.5)"
                        },
                        "div": {
                            "padding": "1px"
                        }
                    },
                    key=result.id,
                    on_click=lambda: add_page(name, result)
                )
    
    st.session_state["search_text"] = search_text
    st.session_state["search_raw_results"] = search_raw_results