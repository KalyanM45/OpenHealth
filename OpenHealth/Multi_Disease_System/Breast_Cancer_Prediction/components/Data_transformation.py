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
from sklearn.preprocessing import StandardScaler, OrdinalEncoder


class DataTransformation:
    def __init__(self):
        pass
            
    
    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Breast Cancer Disease: Read train and test data complete")
            logging.info(f'Breast Cancer Disease: Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Breast Cancer Disease: Test Dataframe Head : \n{test_df.head().to_string()}')

            train_df['diagnosis'] = train_df['diagnosis'].apply(lambda val: 1 if val == 'M' else 0)
            test_df['diagnosis'] = test_df['diagnosis'].apply(lambda val: 1 if val == 'M' else 0)

            
            target_column_name = 'diagnosis'
            drop_columns = [target_column_name, 'id', 'Unnamed: 32', 'radius_mean', 'perimeter_mean', 'area_mean',
                            'concavity_mean', 'radius_se', 'perimeter_se', 'radius_worst', 'perimeter_worst']
            
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]      

            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            logging.info("Breast Cancer Disease: Splitting input and target features complete")

            
            train_arr = np.c_[np.array(input_feature_train_df), np.array(target_feature_train_df)]
            test_arr = np.c_[np.array(input_feature_test_df), np.array(target_feature_test_df)]

            return (train_arr,test_arr)
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise customexception(e,sys)