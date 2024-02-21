import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.logger import logging
from sklearn.metrics import accuracy_score
from src.exception import customexception
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # Configure API key
vision_model = genai.GenerativeModel('gemini-pro-vision') # Initialize Gemini Pro Vision Model
text_model = genai.GenerativeModel('gemini-pro')

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise customexception(e, sys)
    
def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for model_name, model in models.items():
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            test_model_score = accuracy_score(y_test, y_test_pred)
            report[model_name] = test_model_score
        return report
    except Exception as e:
        logging.info('Exception occurred during model training')
        raise customexception(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise customexception(e,sys)
    
def gen_from_image(prompt,imagefile):
    vresponse = vision_model.generate_content(prompt, imagefile)
    return vresponse.text

def gen_from_text(prompt):
    tresponse = text_model.generate_content(prompt)
    return tresponse.text

def prompt(query):
    prompt = f"""Imagine you are a medical expert and you are giving accurate medical advice to a patient. 
        You are presented with a medical query and asked to provide a response with a detailed explanation. 
        Note that dont mention any inaccurate or misleading information.
        Also dont provide false or misleading information. Dont provide the query again in the response.

        Medical Query: {query}

        The Response Text should be in this format: (Just use the below headings)

        Disease Description:
        Symptoms:
        Causes:
        Treatment:
        Prevention:"""
    return prompt

def recognition_prompt(query):
    image_prompt = f'''
    medicine recognition system capable of identifying detailed medications not only from images of tablets but also from various 
    other forms such as capsules, liquids, or even packaging labels. The system should be able to identify medications
    - provide a detailed response about the image.
    - Please ensure the generated content is accurate and clinically relevant.
    - Please don't provide false and misleading information.
    - Additionally, {query}

if the image is not related to medical or healthcare, please provide a message saying "Please Provide Valid Medical Image".'''