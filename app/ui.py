import streamlit as st
from app.utils import get_response
from model.model import generate_response, generate_response_no_image
def chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []


    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def message_box(model, processor):
    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Thinking..."):
            response = generate_response_no_image(model, processor, prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

def message_box_no_image(model, processor):
    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Thinking..."):
            response = generate_response_no_image(model, processor, prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
