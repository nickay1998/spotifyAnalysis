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

def get_image(url, width = 0, height = 0):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    if width != 0 and height != 0:
        image = image.resize((height, width))
    elif width != 0:
        image = image.resize((width, int(image.height * image.width / width)))
    elif height != 0:
        image = image.resize((int(image.width * height / image.height), height))

    return image