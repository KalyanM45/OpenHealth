import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
text_model = genai.GenerativeModel('gemini-pro') 

def brain_tumour1(disease, tumor_type):
    prompt = f"Give me information about the brain disease for this suffering type glioma tumour in the following paragraph format:\
        Disease Name: \
        Disease Description:\
        Disease Symptoms:\
        Disease Treatment:\
        Disease Food to Eat:\
        Disease Food to Avoid:"  
        # Generate information based on the disease and tumor type
    answer = text_model.generate_content(prompt) # Replace with actual generated content
    ans = answer.replace('*', '\n') 
    return ans

def brain_tumour2(disease, tumor_type):
    prompt = f"Give me information about the brain disease for this suffering type meningioma tumour in the following paragraph format:\
        Disease Name: \
        Disease Description:\
        Disease Symptoms:\
        Disease Treatment:\
        Disease Food to Eat:\
        Disease Food to Avoid:"  
        # Generate information based on the disease and tumor type
    answer = text_model.generate_content(prompt) # Replace with actual generated content
    ans = answer.replace('*', '\n') 
    return ans

def brain_tumour3(disease, tumor_type):
    prompt = f"Give me information about the brain disease for this suffering type pituatary tumour in the following paragraph format:\
        Disease Name: \
        Disease Description:\
        Disease Symptoms:\
        Disease Treatment:\
        Disease Food to Eat:\
        Disease Food to Avoid:"  
        # Generate information based on the disease and tumor type
    answer = text_model.generate_content(prompt) # Replace with actual generated content
    ans = answer.replace('*', '\n') 
    return ans