import streamlit as st

def show_details():
    title = st.session_state["nav"].title
    st.write(title)