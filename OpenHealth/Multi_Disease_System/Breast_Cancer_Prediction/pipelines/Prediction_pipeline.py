import os
import sys
import pandas as pd
from src.logger import logging
from src.utils import load_object
from src.exception import customexception

class PredictBCancer:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:            
            preprocessor_path=os.path.join("Artifacts","Breast_Cancer_Disease","BCancer_Preprocessor.pkl")
            model_path=os.path.join("Artifacts","Breast_Cancer_Disease","BCancer_Model.pkl")
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            #scaled_data=preprocessor.transform(features)
            pred=model.predict(features)
            return pred

        except Exception as e:
            raise customexception(e,sys)
    
class BCancer_Data:
    
    def __init__(self,
                texture_mean: float,
                smoothness_mean: float,
                compactness_mean: float,
                concave_points_mean: float,
                symmetry_mean: float,
                fractal_dimension_mean: float,
                texture_se: float,
                area_se: float,
                smoothness_se: float,
                compactness_se: float,
                concavity_se: float,
                concave_points_se: float,
                symmetry_se: float,
                fractal_dimension_se: float,
                texture_worst: float,
                area_worst: float,
                smoothness_worst: float,
                compactness_worst: float,
                concavity_worst: float,
                concave_points_worst: float,
                symmetry_worst: float,
                fractal_dimension_worst: float):
        
        self.texture_mean = texture_mean
        self.smoothness_mean = smoothness_mean
        self.compactness_mean = compactness_mean
        self.concave_points_mean = concave_points_mean
        self.symmetry_mean = symmetry_mean
        self.fractal_dimension_mean = fractal_dimension_mean
        self.texture_se = texture_se
        self.area_se = area_se
        self.smoothness_se = smoothness_se
        self.compactness_se = compactness_se
        self.concavity_se = concavity_se
        self.concave_points_se = concave_points_se
        self.symmetry_se = symmetry_se
        self.fractal_dimension_se = fractal_dimension_se
        self.texture_worst = texture_worst
        self.area_worst = area_worst
        self.smoothness_worst = smoothness_worst
        self.compactness_worst = compactness_worst
        self.concavity_worst = concavity_worst
        self.concave_points_worst = concave_points_worst
        self.symmetry_worst = symmetry_worst
        self.fractal_dimension_worst = fractal_dimension_worst

            
                
    def get_data_as_dataframe(self):
            try:
                custom_data_input_dict = {
                    'texture_mean': [self.texture_mean],
                    'smoothness_mean': [self.smoothness_mean],
                    'compactness_mean': [self.compactness_mean],
                    'concave_points_mean': [self.concave_points_mean],
                    'symmetry_mean': [self.symmetry_mean],
                    'fractal_dimension_mean': [self.fractal_dimension_mean],
                    'texture_se': [self.texture_se],
                    'area_se': [self.area_se],
                    'smoothness_se': [self.smoothness_se],
                    'compactness_se': [self.compactness_se],
                    'concavity_se': [self.concavity_se],
                    'concave_points_se': [self.concave_points_se],
                    'symmetry_se': [self.symmetry_se],
                    'fractal_dimension_se': [self.fractal_dimension_se],
                    'texture_worst': [self.texture_worst],
                    'area_worst': [self.area_worst],
                    'smoothness_worst': [self.smoothness_worst],
                    'compactness_worst': [self.compactness_worst],
                    'concavity_worst': [self.concavity_worst],
                    'concave_points_worst': [self.concave_points_worst],
                    'symmetry_worst': [self.symmetry_worst],
                    'fractal_dimension_worst': [self.fractal_dimension_worst]
                }

                df = pd.DataFrame(custom_data_input_dict)
                print(df)
                logging.info('Dataframe Gathered')
                return df
            except Exception as e:
                logging.info('Exception Occured in prediction pipeline')
                raise customexception(e,sys)