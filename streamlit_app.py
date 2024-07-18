import streamlit as st
from login import get_access_token
import streamlit_antd_components as sac
from utilities.search import search
from utilities.requester import get_image
from utilities.images import crop_center_square
from classes import Album, Artist, Track
from streamlit_js_eval import streamlit_js_eval
from PIL import Image

if __name__ == '__main__':
    st.set_page_config(page_title="Spotify Analysis", layout="wide")
    window_width = streamlit_js_eval(js_expressions='window.innerWidth', key = 'SCR')
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        
    if not st.session_state["logged_in"]:
        get_access_token()
        st.toast(f"Successfully acquired access token: " + st.session_state["access_token"], icon="✅")
    
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

            grouped_list = [search_results[display_type][i:i+5] for i in range(0, len(search_results[display_type]), 5)]
            for group in grouped_list:
                cols = st.columns(5)
                for i, result in enumerate(group):
                    with cols[i].container(border=True):                    
                        name = result.name
                        if len(result.name) >= window_width * 0.023:
                            name = name[:int(window_width * 0.023)] + '...'
                        if len(result.images) == 0:
                            st.image(Image.open("./assets/blank.png"), caption=name)
                        else:
                            st.image(crop_center_square(get_image(result.images[0]["url"])), caption=name)
                        #st.image(get_image(result.images[0]["url"]), width=int(window_width*0.17))