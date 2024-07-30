import streamlit as st

def write_center(text):
    centered_text = f'<p style="text-align:center;">{text}</p>'
    st.markdown(centered_text, unsafe_allow_html=True)