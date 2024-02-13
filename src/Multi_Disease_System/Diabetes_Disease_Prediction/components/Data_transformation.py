import os
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_object
from src.exception import customexception
from sklearn.preprocessing import StandardScaler


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('Artifacts','Diabetes_Disease','Diabetes_Preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformation(self):
        
        try:
            logging.info('Diabetes Disease Prediction: Data Transformation initiated')

            numerical_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
            categorical_cols = []

            logging.info(f'Diabetes Disease Prediction: Numerical Columns : {numerical_cols}')
            logging.info(f'Diabetes Disease Prediction: Categorical Columns : {categorical_cols}')

            logging.info('Diabetes Disease Prediction: Numerical Pipeline Initiated')
                
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise customexception(e,sys)
            
    
    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Diabetes Disease Prediction: Read train and test data complete")
            logging.info(f'Diabetes Disease Prediction: Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Diabetes Disease Prediction: Test Dataframe Head : \n{test_df.head().to_string()}')
            
            preprocessing_obj = self.get_data_transformation()
            
            target_column_name = 'Outcome'
            drop_columns = [target_column_name]
            
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]          
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            logging.info("Diabetes Disease Prediction: Splitting input and target features complete")
            
            scaler = StandardScaler()
            input_feature_train_arr=scaler.fit_transform(input_feature_train_df)
            input_feature_test_arr=scaler.transform(input_feature_test_df)
            logging.info("Diabetes Disease Prediction: Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            #save_object(
            #    file_path=self.data_transformation_config.preprocessor_obj_file_path,
            #    obj=preprocessing_obj)
            
            logging.info("Diabetes Disease Prediction: Preprocessing pickle file saved")
            return (train_arr,test_arr)
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise customexception(e,sys)