import streamlit as st


if "messages" not in st.session_state:
    st.session_state.messages = []

st.set_page_config(page_title="Multimodal Chatbot", page_icon="🧠")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = f"You said: {prompt}"
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()


