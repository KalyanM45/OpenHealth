import os
import streamlit as st
from PIL import Image
from src.utils import recognition_prompt
from dotenv import load_dotenv
import google.generativeai as genai

st.set_page_config(page_title="Medical Image Analysis", page_icon=":microscope:", layout="centered", initial_sidebar_state="auto")

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Configure Google Generative AI
vis_model = genai.GenerativeModel('gemini-pro-vision')  # Loaded the Pro-Vision model
text_model = genai.GenerativeModel('gemini-pro')  # Loaded the Pro model

# Function to generate content
def gen_image(prompt, image):
    response = vis_model.generate_content(image)
    return response.text

def validate(validation_prompt):
    vresponse = text_model.generate_content(validation_prompt)
    return vresponse.text

st.title('Medical Image Analysis')

query = st.text_input("Enter any additional information you want to provide to the model.")
question = recognition_prompt(query)
uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    response_text = gen_image(question, image)
    st.write(response_text)