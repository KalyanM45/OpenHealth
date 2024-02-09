import os
import streamlit as st
from PIL import Image
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
image_prompt = f'''
    medicine recognition system capable of identifying detailed medications not only from images of tablets but also from various 
    other forms such as capsules, liquids, or even packaging labels. The system should be able to identify medications
    - provide a detailed response about the image.
    - If you dont find any medical equipment, print please provide a detailed response about the image.
    - Please ensure the generated content is accurate and clinically relevant.
    - Please don't provide false and misleading information.
    - Additionally, {query}
'''

uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    response_text = gen_image(image_prompt, image)
    st.write(response_text)