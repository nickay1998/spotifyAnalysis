import streamlit as st
from utilities.requester import post_data

def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = { "Content-Type": "application/x-www-form-urlencoded" }
    data = { "grant_type": "client_credentials", "client_id": st.secrets["API_KEY"], "client_secret": st.secrets["API_SECRET"] }

    access_token_response = post_data(url, headers, data)
    st.session_state["access_token"] = access_token_response["access_token"]
    st.session_state["logged_in"] = True
    print("Access key acquired!")