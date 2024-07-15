import requests
import streamlit as st
from PIL import Image
from io import BytesIO

def get_data(url):
    headers = {"Authorization": "Bearer " + st.session_state["access_token"]}
    response = requests.get(url, headers = headers)

    if response.status_code != 200:
        print(f"Error occurred. Status code: {response.status_code}")
    
    return response.json()

def post_data(url, headers, data):
    response = requests.post(url, headers = headers, data = data)

    if response.status_code != 200:
        print(f"Error occurred. Status code: {response.status_code}")
    
    return response.json()

def get_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    
    return image