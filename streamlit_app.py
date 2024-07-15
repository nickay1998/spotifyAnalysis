import streamlit as st
from login import get_access_token
import streamlit_antd_components as sac
from utilities.search import search
from utilities.requester import get_image
from classes import Album, Artist, Track

if __name__ == '__main__':
    if "access_token" not in st.session_state:
        if st.button("Get access token!"):
            get_access_token()
            st.toast(f"Successfully acquired access token: " + st.session_state["access_token"], icon="✅")

    if "access_token" in st.session_state:
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

            for result in search_results[display_type]:
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.image(get_image(result.images[0]["url"]), use_column_width=True)
                with col2:
                    st.write(result.name)