import streamlit as st
from login import check_login
import streamlit_antd_components as sac
from utilities.search import search
from utilities.requester import get_image
from utilities.images import crop_center_square
from classes import Album, Artist, Track
from streamlit_js_eval import streamlit_js_eval
from PIL import Image
from streamlit_card import card

if __name__ == '__main__':
    st.set_page_config(page_title="Spotify Analysis", layout="wide")

    with open("./styles/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    window_width = streamlit_js_eval(js_expressions='window.innerWidth', key='SCR')
    
    check_login()

    if st.session_state["logged_in"]:
        with st.form(key="Search"):
            search_text = st.text_input("Search")
            submit_button = st.form_submit_button(label="Submit")

        if search_text != "":
            search = search(search_text)
            search_results = {}
            search_types = []
            for search_type in search:
                search_results[search_type] = []
                search_types.append(sac.TabsItem(label=search_type))

                for result in search[search_type]["items"]:
                    print(f"{search_type}: {result['name']}")

                    if search_type == "albums":
                        search_results[search_type].append(Album(result))
                    elif search_type == "artists":
                        search_results[search_type].append(Artist(result))
                    elif search_type == "tracks":
                        search_results[search_type].append(Track(result))

            display_type = sac.tabs(search_types, align='center', use_container_width=True)
            columns = int(window_width / 270)
            grouped_list = [search_results[display_type][i:i+columns] for i in range(0, len(search_results[display_type]), columns)]
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
                            }
                        )