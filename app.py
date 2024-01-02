import os
import sys
import subprocess
from PIL import Image
import google.generativeai as genai
from flask import Flask, render_template,request

# Setting Gemini Large Language Model Credentials
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # Configure API key
vision_model = genai.GenerativeModel('gemini-pro-vision') # Initialize Gemini Pro Vision Model
text_model = genai.GenerativeModel('gemini-pro') # Initialize Gemini Pro Model

app = Flask(__name__)

def gen_from_image(prompt,imagefile):
    pass

def gen_from_text(prompt):
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/medrecog')
def medrecog():
    if request.method == 'POST':
        med_prompt = '''
                    - Generate a very detailed medical description for the given image.
                    - Identify and describe any relevant medical conditions, anomalies, or abnormalities present in the image.
                    - Additionally, provide insights into any potential treatments or recommended actions based on the observed medical features.
                    - Please ensure the generated content is accurate and clinically relevant.
                    - Please don't provide false and misleading information.
                    '''
        
        validation_prompt = f"Check if the provided description is related to the medical field. Just Reply with 'Yes' or 'No'. Response: {response}"
        image_file = request.files['file']
        imagefile = Image.open(image_file)
        response = gen_from_image(med_prompt,imagefile)
        validation_response = gen_from_text(validation_prompt)

        if validation_response == 'Yes':
            render_template('medrecog.html',response=response)
        else:
            render_template('medrecog.html',response="Please provide a valid medical image.")

    render_template('medrecog.html')

@app.route('/conditional')

@app.route('/', methods=['GET', 'POST'])
def conditional():
    if request.method == 'POST':
        try:
            user_input = request.form['user_input']
        except:
            return render_template('index.html', error="Please enter a valid input.")

        prompt = f"""Imagine you are a medical expert and you are giving accurate medical advice to a patient. 
        You are presented with a medical query and asked to provide a response with a detailed explanation. 
        Note that dont mention any inaccurate or misleading information.

        Medical Query: {user_input}

        Key Details:
        - Provide precise information related to the patient's medical concern.
        - Indicate if any diagnostic tests or examinations have been performed.
        - Specify the current medications or treatments prescribed.
        - The response should be in a paragraph format but not in point-wise.
        - If only a specific disease name is mentioned, response must contain the symptoms, causes, and treatment of the disease with respective headings.

        Guidelines:
        - Use clear and concise language.
        - The vocabulary should be appropriate for the medical context.
        - Include specific parameters or considerations within the medical context.
        - If the response contains a list of items, convert it into a paragraph format.
        - Avoid using abbreviations or acronyms.
        - Avoid Headings and Sub hheadings just give me the complete response in a paragraph format.
        - Refrain from presenting inaccurate or ambiguous information.
        - Ensure the query is focused and not overly broad."""

        # Get Gemini response
        gemini_response = gen_from_text(prompt)

        return render_template('index.html', user_input=user_input, response=gemini_response)

    return render_template('index.html')

@app.route('/chatbot')
def chat():
    pass


if __name__ == '__main__':
    app.run(debug=True)