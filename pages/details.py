import streamlit as st
import utilities.streamlit_extensions as ste
from streamlit_card import card
from datetime import datetime
from utilities.datetime_extensions import convert_to_date_string, convert_to_datetime, calculate_time_since_string

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
    
    ste.write_center(data.name)
    ste.write_center(f"By {', '.join(data.artists)}")
    
    ste.write_center(f"Released {calculate_time_since_string(data.release_date)} on {convert_to_date_string(convert_to_datetime(data.release_date))}")