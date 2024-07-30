import streamlit as st
import utilities.streamlit_extensions as ste
from streamlit_card import card

def show_details():
    title = st.session_state["nav"].title
    data = st.session_state["page_details"][title]

    if len(data.images) > 0:
        image_link = data.images[0]["url"]
    else:
        image_link = ""
    
    card(
        title="",
        text="",
        image=image_link,
        styles={
            "card": {
                "width": "60%", "height": "width", "border-radius": "10px", "aspect-ratio": "1","box-shadow": "0 0 0px rgba(0,0,0,0.5)", "margin": "1px"
            },
            "filter": {
                "background-color": "rgba(0, 0, 0, 0)"
            },
            "div": {
                "padding": "1px"
            }
        },
        url=image_link
    )
    
    ste.write_center(f"{data.name} - {', '.join(data.artists)}")