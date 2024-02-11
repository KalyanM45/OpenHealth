import warnings
warnings.simplefilter('ignore')

import os
import sys
import pickle
import subprocess
import numpy as np
from PIL import Image
from src.utils import gen_from_image, gen_from_text
from flask import Flask, render_template,request,redirect,url_for
from src.Multi_Disease_System.Parkinsons_Disease_Prediction.pipelines.Prediction_pipeline import CustomData, PredictPipeline
from src.Multi_Disease_System.Breast_Cancer_Prediction.pipelines.Prediction_pipeline import CustomData, PredictPipeline
from src.Multi_Disease_System.Heart_Disease_Prediction.pipelines.Prediction_pipeline import CustomData, PredictPipeline


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect')
def redirect_to_landing():
    return redirect(url_for('landing'))

@app.route('/landing')
def landing():
    return render_template('index')

@app.route('/chatbot')
def run_streamlit():
    subprocess.Popen(['streamlit', 'run', 'src/GeminiMed/app.py'])
    return redirect(url_for('index'))

@app.route('/recognition')
def run_streamlit1():
    subprocess.Popen(['streamlit', 'run', 'src/MedicineRecognition/app.py'])
    return redirect(url_for('index'))

@app.route('/brain')
def brain():
    return render_template('brain_tumour.html')

@app.route('/bcancer', methods=["GET", "POST"])
def brain_post():
    if request.method == 'POST':
        data = CustomData(
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
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)
        result = round(pred[0], 2)
        return render_template('bcancer.html', final_result=result)
    
    return render_template('bcancer.html')

@app.route('/diabetes')
def bcancer_post():
        return render_template('diabetes.html')

@app.route('/heart', methods=["GET", "POST"])
def heart():
    if request.method == "POST":
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
    
    return render_template("heart.html")

@app.route('/kidney')
def kidney():
    return render_template('kidney.html')

@app.route('/liver')
def liver():
    return render_template('liver.html')

@app.route('/lung')
def lung():
    return render_template('lung.html')

@app.route('/malaria')
def malaria():
    return render_template('malaria.html')

@app.route('/ocular')
def pneumonia():
    return render_template('ocular.html')

@app.route('/parkinsons', methods=["GET", "POST"])
def parkinsons():
    if request.method == 'POST':
        data = CustomData(
                MDVPFO=float(request.form.get("MDVPFO")),
                MDVPFHI=float(request.form.get("MDVPFHI")),
                MDVPFLO=float(request.form.get("MDVPFLO")),
                MDVPJ=float(request.form.get("MDVPJ")),
                RPDE=float(request.form.get("RPDE")),
                DFA=float(request.form.get("DFA")),
                spread2=float(request.form.get("spread2")),
                D2=float(request.form.get("D2")))
    
        final_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)
        result = round(pred[0], 2)
        return render_template("parkinsons.html", final_result=result)
    
    return render_template('parkinsons.html')

@app.route('/skincancer')
def skin():
    return render_template('skin.html')

@app.route('/error')
def stroke():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)