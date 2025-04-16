from PIL import Image
import torch
from transformers import Blip2Processor, Blip2ForConditionalGeneration, AutoTokenizer, AutoModelForCausalLM
import streamlit as st

@st.cache_resource
def load_model():
    processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
    model = Blip2ForConditionalGeneration.from_pretrained(
        "Salesforce/blip2-opt-2.7b",
        torch_dtype=torch.float16
    )
    model.to("cuda" if torch.cuda.is_available() else "cpu")
    return model, processor

def generate_response(model, processor, input_text):
    dummy_image = Image.new("RGB", (224, 224), (255, 255, 255))
    prompt = input_text

    inputs = processor(images=dummy_image, text=prompt, return_tensors="pt").to(model.device)
    generated_ids = model.generate(**inputs)
    output = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return output

def generate_response_no_image(model, tokenizer, input_text):
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True).to("cuda")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]
    outputs = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if input_text.lower() in response.lower():
        response = response.lower().replace(input_text.lower(), "").strip()
    print(response)
    return response


@st.cache_resource
def load_model_no_image():
    model_name = "Qwen/Qwen2.5-7B"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True
    )
    device = next(model.parameters()).device
    print(f"Model loaded on device: {device}")
    
    model.eval()
    return model, tokenizer