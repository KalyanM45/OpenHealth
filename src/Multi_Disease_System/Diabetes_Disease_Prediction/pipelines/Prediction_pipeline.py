import os
import sys
import pandas as pd
from src.logger import logging
from src.utils import load_object
from src.exception import customexception

class PredictDiabetes:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:            
            preprocessor_path=os.path.join("Artifacts","Diabetes_Disease","Diabetes_Preprocessor.pkl")
            model_path=os.path.join("Artifacts","Diabetes_Disease","Diabetes_Model.pkl")
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            scaled_data=preprocessor.transform(features)
            pred=model.predict(scaled_data)
            return pred

        except Exception as e:
            raise customexception(e,sys)
        
class Diabetes_Data:
    
    def __init__(self,
                 pregnancies: int,
                 Glucose: int,
                 BloodPressure: int,
                 skin_thickness: int,
                 insulin: int,
                 BMI: float,
                 DiabetesPedigreeFunction: float,
                 Age: int):
        
        self.pregnancies = pregnancies
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.skin_thickness = skin_thickness
        self.insulin = insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age

            
                
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'pregnancies': [self.pregnancies],
                'Glucose': [self.Glucose],
                'BloodPressure': [self.BloodPressure],
                'skin_thickness': [self.skin_thickness],
                'insulin': [self.insulin],
                'BMI': [self.BMI],
                'DiabetesPedigreeFunction': [self.DiabetesPedigreeFunction],
                'Age': [self.Age]
            }

            df = pd.DataFrame(custom_data_input_dict)
            print(df)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occurred in prediction pipeline')
            raise customexception(e,sys)