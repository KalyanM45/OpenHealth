import os
import streamlit as st
from src.utils import prompt
from dotenv import load_dotenv
import google.generativeai as genai

st.set_page_config(
    page_title="Medical Expert Advisor",page_icon="🧊",layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

st.title('OpenHealth: GPT-4.5')

user_input = st.text_input("Enter Your Medical Query Here:")

question = prompt(user_input)

if st.button('Get Advice'):
    gemini_response = get_gemini_response(question)
    st.write(gemini_response)