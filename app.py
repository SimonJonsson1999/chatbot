import streamlit as st
from app.ui import display_chat

st.set_page_config(page_title="Chatbot", page_icon="🧠")
st.title("Minimal Chatbot")


display_chat()


