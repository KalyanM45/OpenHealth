import os
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_object
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.exception import customexception
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('Artifacts','Heart_Disease','Heart_Preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformation(self):
        
        try:
            logging.info('Heart Disease Prediction: Data Transformation initiated')
            numerical_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
            logging.info(f'Heart Disease Prediction: Numerical Columns : {numerical_cols}')
            logging.info('Heart Disease Prediction: Numerical Pipeline Initiated')
            preprocessor = StandardScaler()
            return preprocessor 
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise customexception(e,sys)
            
    
    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Heart Disease Prediction: Read train and test data complete")
            logging.info(f'Heart Disease Prediction: Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Heart Disease Prediction: Test Dataframe Head : \n{test_df.head().to_string()}')
            
            preprocessing_obj = self.get_data_transformation()
            
            target_column_name = 'target'
            drop_columns = [target_column_name]
            
            x_train = train_df.drop(columns=drop_columns,axis=1)
            y_train=train_df[target_column_name]  

            x_test=test_df.drop(columns=drop_columns,axis=1)
            y_test=test_df[target_column_name]
            logging.info("Heart Disease Prediction: Splitting input and target features complete")
            
            preprocessed_x_train=preprocessing_obj.fit_transform(x_train)
            preprocessed_x_test =preprocessing_obj.transform(x_test)
            logging.info("Heart Disease Prediction: Applying preprocessing object on training and testing datasets.")


            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj)
            
            logging.info("Heart Disease Prediction: Preprocessing pickle file saved")
            return (preprocessed_x_train,y_train,preprocessed_x_test,y_test)
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise customexception(e,sys)