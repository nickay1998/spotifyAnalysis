import streamlit as st
from login import get_access_token

if st.button("Get access token!"):
    get_access_token()
    st.success(f"Successfully acquired access token: " + st.session_state["access_token"], icon="✅")