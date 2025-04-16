import streamlit as st
from app.utils import get_response
def display_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []


    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = get_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
