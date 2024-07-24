import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from application import search_page, check_login

if __name__ == '__main__':
    
    st.set_page_config(page_title="Spotify Analysis", layout="wide")
    
    if 'SELECTION' not in st.session_state:
        st.session_state['SELECTION'] = 'value'

    with open("./styles/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.session_state["window_width"] = window_width = streamlit_js_eval(js_expressions='window.innerWidth', key='SCR')
    
    check_login()

    if st.session_state["logged_in"]:
        search_page()