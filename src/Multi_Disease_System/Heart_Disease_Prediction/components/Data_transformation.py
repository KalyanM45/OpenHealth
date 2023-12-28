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
            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())])

            preprocessor = ColumnTransformer([('num_pipeline',num_pipeline,numerical_cols)])
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
            
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]          
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            logging.info("Heart Disease Prediction: Splitting input and target features complete")
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            logging.info("Heart Disease Prediction: Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj)
            
            logging.info("Heart Disease Prediction: Preprocessing pickle file saved")
            return (train_arr,test_arr)
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise customexception(e,sys)