import streamlit as st
from app.ui import chat, message_box, message_box_no_image
from model.model import load_model, load_model_no_image
import os
import asyncio
import torch._classes
torch._classes.__path__ = [] 
try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
st.set_page_config(page_title="Chatbot", page_icon="🧠")
st.title("Minimal Chatbot")
image = None
chat()
if image:
    model, processor = load_model()
    message_box(model, processor)
else:
    model, tokenizer = load_model_no_image()
    message_box_no_image(model, tokenizer)






