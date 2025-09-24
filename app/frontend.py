import streamlit as st
import requests
import pickle
from transformers import AutoTokenizer
import config

src_sent_tokenizer = AutoTokenizer.from_pretrained("google-T5/t5-base")

st.title("English to hindi Translator")

input_sent = st.text_area("Enter your english sentence here")

if st.button("Translate"):
    if(len(src_sent_tokenizer.tokenize(input_sent)))>config.ns:
        st.warning("The input sentence is too long. Please enter a shorter sentence.")
    if input_sent.strip() == "":
        st.warning("Please enter a valid English sentence.")
    else:
        response = requests.post("http://localhost:8000/translate", json={"text": input_sent})
        
        if response.status_code == 200:
            translated_text = response.json().get("hindi_translation", "")
            st.success("Translation successful!")
            st.write("Hindi Translation: " + translated_text)
        else:
            st.error("API Error : Translation failed. Please try again.",response.text)
            