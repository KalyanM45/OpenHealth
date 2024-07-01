import os
import sys
import logging
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level = logging.INFO, 
                    filename = LOG_FILEPATH, 
                    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

import os
import sys
import pickle
import numpy as np
import pandas as pd

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

class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
        