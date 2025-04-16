# 🧠 Multimodal Chatbot

A local AI-powered chatbot built with [BLIP-2](https://huggingface.co/Salesforce/blip2-opt-2.7b) and Streamlit that can answer questions about images. Users can upload an image and ask questions about it.

---

## 🚀 Features

### ✅ Completed
- [x] Streamlit Chat UI (chat-style interaction) without image
- [x] Setup structure for unittests
### 🧱 In Progress
- [x] Load BLIP-2
- [x] Session state for storing interactions
- [x] Generate response from BLIP-2 
- [x] Show dialog with BLIP-2 in CHAT UI
- [x] Add a text-only fallback chatbot (QWEN2.5 7B)
- [x] Add loading spinner while generating response
### 🔜 To Do
- [ ] Setup unit and function tests
- [ ] Upload an image
- [ ] Error handling (e.g. unsupported image format)
- [ ] Drag & drop image upload
- [ ] Support for CPU fallback
- [ ] Use BLIP-2 to analyze image and generate response
- [ ] Display image and response in the UI
- [ ] Save conversation history
- [ ] Let user download chat as PDF or .txt
- [ ] Package as a Hugging Face Space or Streamlit Cloud app
- [ ] Finetune BLIP-2 for specilised bot.



## 🛠️ Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/simonjonsson1999/chatbot.git
cd chatbot
