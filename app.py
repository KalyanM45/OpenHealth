import os
import sys
from PIL import Image
from src.utils import gen_from_image, gen_from_text
from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/redirect')
def redirect_to_landing():
    return redirect(url_for('landing'))

@app.route('/landing')
def landing():
    return render_template('index.html')

@app.route('/brain')
def brain():
    return render_template('brain_tumour.html')

@app.route('/bcancer')
def brain_post():
        return render_template('bcancer.html')

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