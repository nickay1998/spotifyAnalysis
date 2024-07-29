import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from utilities import check_login

if __name__ == '__main__':
    
    st.set_page_config(page_title="Spotify Analysis", layout="wide")

    with open("./styles/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.session_state["window_width"] = window_width = streamlit_js_eval(js_expressions='window.innerWidth', key='SCR')
    
    check_login()

    if "page_details" not in st.session_state:
        st.session_state["page_details"] = {}

    if st.session_state["logged_in"]:
        
        if "pages" in st.session_state:
            pages = st.session_state["pages"]
        else:
            pages = st.session_state["pages"] = [st.Page("./pages/search.py", title="Search")]
        
        st.session_state["nav"] = nav = st.navigation(pages)

        nav.run()