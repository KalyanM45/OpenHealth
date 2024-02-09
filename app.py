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

# Loading the Model
bcancer_model = pickle.load(open('Artifacts/Breast_Cancer_Disease/BCancer_Model.pkl', 'rb'))
bcancer_preprocessor = pickle.load(open('Artifacts/Breast_Cancer_Disease/BCancer_Preprocessor.pkl', 'rb'))

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

@app.route('/bcancer')
def brain_post():
    try:
        texture_mean = float(request.form['texture_mean'])
        smoothness_mean = float(request.form['smoothness_mean'])
        compactness_mean = float(request.form['compactness_mean'])
        concave_points_mean = float(request.form['concave_points_mean'])
        symmetry_mean = float(request.form['symmetry_mean'])
        fractal_dimension_mean = float(request.form['fractal_dimension_mean'])
        texture_se = float(request.form['texture_se'])
        area_se = float(request.form['area_se'])
        smoothness_se = float(request.form['smoothness_se'])
        compactness_se = float(request.form['compactness_se'])
        concavity_se = float(request.form['concavity_se'])
        concave_points_se = float(request.form['concave_points_se'])
        symmetry_se = float(request.form['symmetry_se'])
        fractal_dimension_se = float(request.form['fractal_dimension_se'])
        texture_worst = float(request.form['texture_worst'])
        area_worst = float(request.form['area_worst'])
        smoothness_worst = float(request.form['smoothness_worst'])
        compactness_worst = float(request.form['compactness_worst'])
        concavity_worst = float(request.form['concavity_worst'])
        concave_points_worst = float(request.form['concave_points_worst'])
        symmetry_worst = float(request.form['symmetry_worst'])
        fractal_dimension_worst = float(request.form['fractal_dimension_worst'])

        features = np.array([[texture_mean, smoothness_mean, compactness_mean, concave_points_mean,
                            symmetry_mean, fractal_dimension_mean, texture_se, area_se,
                            smoothness_se, compactness_se, concavity_se, concave_points_se,
                            symmetry_se, fractal_dimension_se, texture_worst, area_worst,
                            smoothness_worst, compactness_worst, concavity_worst, concave_points_worst,
                            symmetry_worst, fractal_dimension_worst]])

        prediction = bcancer_model.predict(features)

        if prediction[0] == 0:
            result = 'Benign'
        else:
            result = 'Malignant'
        
        return render_template('bcancer.html', result=result)
    except:
        return render_template('error.html')

@app.route('/diabetes')
def bcancer_post():
        return render_template('diabetes.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

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

@app.route('/parkinsons')
def ocular():
    return render_template('parkinsons.html')

@app.route('/skincancer')
def parkinsons():
    return render_template('skin.html')

@app.route('/error')
def stroke():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)