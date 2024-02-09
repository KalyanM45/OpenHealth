import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

st.set_page_config(
    page_title="Medical Expert Advisor",
    page_icon="🧊",
    layout="centered",
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

st.title('GeminiMed: GPT-4.5')

user_input = st.text_input("Enter Your Medical Query Here:")

prompt = f"""Imagine you are a medical expert and you are giving accurate medical advice to a patient. 
        You are presented with a medical query and asked to provide a response with a detailed explanation. 
        Note that dont mention any inaccurate or misleading information.
        Also dont provide false or misleading information. Dont provide the query again in the response.

        Medical Query: {user_input}

        The Response Text should be in this format: (Just use the below headings)

        Disease Description:
        Symptoms:
        Causes:
        Treatment:
        Prevention:"""

if st.button('Get Advice'):
    gemini_response = get_gemini_response(prompt)
    st.write(gemini_response)