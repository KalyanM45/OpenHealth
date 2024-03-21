import warnings
warnings.simplefilter('ignore')

import os
import cv2
import sys
import pickle
import subprocess
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from src.utils import gen_from_image, gen_from_text, get_med
from flask import Flask, render_template,request,redirect,url_for
from src.Multi_Disease_System.Parkinsons_Disease_Prediction.pipelines.Prediction_pipeline import Parkinsons_Data, PredictParkinsons
from src.Multi_Disease_System.Breast_Cancer_Prediction.pipelines.Prediction_pipeline import BCancer_Data, PredictBCancer
from src.Multi_Disease_System.Diabetes_Disease_Prediction.pipelines.Prediction_pipeline import Diabetes_Data, PredictDiabetes
from src.Multi_Disease_System.Heart_Disease_Prediction.pipelines.Prediction_pipeline import CustomData, PredictPipeline
brain_model = load_model('Artifacts\Brain_Tumour\BrainModel.h5')
kidney_model = load_model('Artifacts\Kidney_Disease\Kidney_Model.h5')
#lung_model = load_model('Artifacts\Lung_Disease\Lung_Model.h5')
livermodel = pickle.load(open('Artifacts\Liver_Disease\Liver_Model.pkl', 'rb'))
#liverpreprocessor = pickle.load(open('Artifacts\Liver_Disease\Liver_Preprocessor.pkl', 'rb'))



app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('landing.html')
    except:
        return render_template('error.html')
    
@app.route('/services')
def index1():
    try:
        return render_template('services.html')
    except:
        return render_template('error.html')
    
'''@app.route('/landing')
def other():
    return render_template('landing.html')'''

@app.route('/chatbot')
def run_streamlit():
    try:
        subprocess.Popen(['streamlit', 'run', 'src/GeminiMed/app.py'])
        return redirect(url_for('index'))
    except:
        return render_template('error.html')


@app.route('/recognition')
def run_streamlit1():
    try:
        subprocess.Popen(['streamlit', 'run', 'src/MedicineRecognition/app.py'])
        return redirect(url_for('index'))
    except:
        return render_template('error.html')

@app.route('/food/<disease>/<tumor_type>', methods=['GET', 'POST'])
def more_info(disease, tumor_type):
    if request.method == 'POST':
        prompt = f"Give me information about the {disease} for this suffering type {tumor_type} in the following paragraph format:\
        Disease Name: \
        Disease Description:\
        Disease Symptoms:\
        Disease Treatment:\
        Disease Food to Eat:\
        Disease Food to Avoid:"  
        # Generate information based on the disease and tumor type
        answer = text_model.generate_content(prompt) # Replace with actual generated content
        ans = answer.replace('*', '\n') 
        return render_template("llm.html", answer=ans)
    return render_template("llm.html", disease=disease, tumor_type=tumor_type)


@app.route('/brain', methods=['GET', 'POST'])
def brain():
    if request.method == 'POST':
        try:
            def preprocess_image(image):
                img = Image.open(image)
                img = img.resize((299, 299))
                img = np.asarray(img)
                img = np.expand_dims(img, axis=0)
                img = img / 255
                return img
            
            class_labels = {0: 'Glioma Tumour', 1: 'Meningioma Tumour', 2: 'No Tumour', 3: 'Pituitary Tumour'}
            file = request.files['file']
            file_path = 'temp.jpg'
            file.save(file_path)
            processed_image = preprocess_image(file_path)
            predictions = brain_model.predict(processed_image)
            prediction_label = class_labels[np.argmax(predictions)]
            confidence = np.max(predictions)
            os.remove(file_path)

            if request.form.get('button') == 'More Info':
                if prediction_label == 'Glioma Tumour':
                    return redirect(url_for('brain_tumour1', disease='brain', tumor_type='glioma'))
                elif prediction_label == 'Meningioma Tumour':
                    return redirect(url_for('brain_tumour2', disease='brain', tumor_type='meningioma'))
                elif prediction_label == 'Pituitary Tumour':
                    return redirect(url_for('brain_tumour3', disease='brain', tumor_type='pituitary'))                
            
            return render_template('brain_tumour.html', prediction=prediction_label)
        except:
            return render_template('error.html')
    return render_template('brain_tumour.html')


@app.route('/bcancer', methods=["GET", "POST"])
def brain_post():
    if request.method == 'POST':
        try:
            data = BCancer_Data(
                texture_mean = float(request.form['texture_mean']),
                smoothness_mean = float(request.form['smoothness_mean']),
                compactness_mean = float(request.form['compactness_mean']),
                concave_points_mean = float(request.form['concave_points_mean']),
                symmetry_mean = float(request.form['symmetry_mean']),
                fractal_dimension_mean = float(request.form['fractal_dimension_mean']),
                texture_se = float(request.form['texture_se']),
                area_se = float(request.form['area_se']),
                smoothness_se = float(request.form['smoothness_se']),
                compactness_se = float(request.form['compactness_se']),
                concavity_se = float(request.form['concavity_se']),
                concave_points_se = float(request.form['concave_points_se']),
                symmetry_se = float(request.form['symmetry_se']),
                fractal_dimension_se = float(request.form['fractal_dimension_se']),
                texture_worst = float(request.form['texture_worst']),
                area_worst = float(request.form['area_worst']),
                smoothness_worst = float(request.form['smoothness_worst']),
                compactness_worst = float(request.form['compactness_worst']),
                concavity_worst = float(request.form['concavity_worst']),
                concave_points_worst = float(request.form['concave_points_worst']),
                symmetry_worst = float(request.form['symmetry_worst']),
                fractal_dimension_worst = float(request.form['fractal_dimension_worst'])
                )
            final_data = data.get_data_as_dataframe()
            predict_pipeline = PredictBCancer()
            pred = predict_pipeline.predict(final_data)
            an = round(pred[0], 2)
            return render_template('bcancer.html', final_result=an)
        except:
            pass
    return render_template('bcancer.html')

@app.route('/diabetes', methods=["GET", "POST"])
def diabetes():
    if request.method == "POST":
        try:
            data = Diabetes_Data(
                pregnancies=request.form.get("pregnancies"),
                Glucose=request.form.get("Glucose"),
                BloodPressure=request.form.get("BloodPressure"),
                skin_thickness=request.form.get("skin_thickness"),
                insulin=request.form.get("insulin"),
                BMI=request.form.get("BMI"),
                DiabetesPedigreeFunction=request.form.get("DiabetesPedigreeFunction"),
                Age=request.form.get("Age"))
            final_data = data.get_data_as_dataframe()
            predict_pipeline = PredictDiabetes()
            pred = predict_pipeline.predict(final_data)
            return render_template("diabetes.html", final_result=pred)
        except Exception as e:
            pass
    return render_template("diabetes.html")

@app.route('/heart', methods=["GET", "POST"])
def heart():
    if request.method == "POST":
        try:
            data = CustomData(
                age=request.form.get("age"),
                sex=request.form.get("sex"),
                cp=(request.form.get("cp")),
                trestbps=(request.form.get("trestbps")),
                chol=(request.form.get("chol")),
                fbs=request.form.get("fbs"),
                restecg=request.form.get("restecg"),
                thalach=(request.form.get("thalach")),
                exang=request.form.get("exang"),
                oldpeak=request.form.get("oldpeak"),
                slope=request.form.get("slope"),
                ca=request.form.get("ca"),
                thal=(request.form.get("thal")))
            final_data = data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_data)
            result = round(pred[0], 2)
            return render_template("heart.html", final_result=result)
        except:
            return render_template("error.html")
    return render_template("heart.html")

@app.route('/kidney', methods=['GET', 'POST'])
def kidney():
    if request.method == 'POST':
        try:
            class_labels = {0: 'Cyst', 1: 'Normal', 2: 'Stone', 3: 'Tumor'}
            file = request.files['file']
            if file.filename == '':
                return render_template('error.html', message='No file selected')
            file_path = 'temp.jpg'
            file.save(file_path)
            img = cv2.imread(file_path)
            img = cv2.resize(img, (150, 150))
            img = img / 255.0
            img = np.expand_dims(img, axis=0)
            predictions = kidney_model.predict(img)
            prediction_label = class_labels[np.argmax(predictions)]
            os.remove(file_path)
            return render_template('kidney.html', prediction=prediction_label)
        except Exception as e:
            return render_template('error.html', message=str(e))
    return render_template('kidney.html')

'''
@app.route('/lung')
def predict():
    if request.method == 'POST':
        img_file = request.files['file']
        img_path = "static/" + img_file.filename
        img_file.save(img_path)

        # Preprocess the image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        # Make prediction
        prediction = lung_model.predict(img_array)
        predicted_class = np.argmax(prediction)

        # Define classes
        classes = ['COVID-19', 'Normal', 'Pneumonia-Bacterial', 'Pneumonia-Viral', 'Tuberculosis']

        return render_template('result.html', img_path=img_path, prediction=classes[predicted_class])
    return render_template('lung.html')'''

@app.route('/liver', methods=['GET', 'POST'])
def liver():
    if request.method == 'POST':
        age = float(request.form['age'])
        gender = int(request.form['gender'])
        total_bilirubin = float(request.form['total_bilirubin'])
        direct_bilirubin = float(request.form['direct_bilirubin'])
        alkaline_phosphotase = float(request.form['alkaline_phosphotase'])
        alamine_aminotransferase = float(request.form['alamine_aminotransferase'])
        aspartate_aminotransferase = float(request.form['aspartate_aminotransferase'])
        total_proteins = float(request.form['total_proteins'])
        albumin = float(request.form['albumin'])
        albumin_globulin_ratio = float(request.form['albumin_globulin_ratio'])
        
        # Preprocess features
        features = np.array([age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase,
                            alamine_aminotransferase, aspartate_aminotransferase, total_proteins,
                            albumin, albumin_globulin_ratio]).reshape(1, -1)
        
        # Make prediction - (livermodel and liverpreprocessor assumed to be defined elsewhere)
        prediction = livermodel.predict(features)[0]
        probability = livermodel.predict_proba(features)[0][1]
        
        # Prepare response
        if prediction == 1:
            result = 'Positive'
        else:
            result = 'Negative'
        
        return render_template('liver.html', prediction=result)

    return render_template('liver.html')


@app.route('/malaria')
def malaria():
    try:
        return render_template('malaria.html')
    except:
        return render_template('error.html')
    

@app.route('/parkinsons', methods=["GET", "POST"])
def parkinsons():
    if request.method == 'POST':
        try:
            data = Parkinsons_Data(
                    MDVPFO=float(request.form.get("MDVPFO")),
                    MDVPFHI=float(request.form.get("MDVPFHI")),
                    MDVPFLO=float(request.form.get("MDVPFLO")),
                    MDVPJ=float(request.form.get("MDVPJ")),
                    RPDE=float(request.form.get("RPDE")),
                    DFA=float(request.form.get("DFA")),
                    spread2=float(request.form.get("spread2")),
                    D2=float(request.form.get("D2")))
            final_data = data.get_data_as_dataframe()
            predict_pipeline = PredictParkinsons()
            pred = predict_pipeline.predict(final_data)
            result = round(pred[0], 2)
            return render_template("parkinsons.html", final_result=result)
        except:
            return render_template("error.html")
    return render_template('parkinsons.html')

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
text_model = genai.GenerativeModel('gemini-pro') 

@app.route('/brain_tumour1')
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
    return render_template("llm.html", answer=ans)

@app.route('/brain_tumour2')
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
    return render_template("llm.html", answer=ans)

@app.route('/brain_tumour3')
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
    return render_template("llm.html", answer=ans)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)