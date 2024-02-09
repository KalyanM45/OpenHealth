import os
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import customexception


class DataTransformation:
    def __init__(self):
        pass            
    
    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Parkinsons Disease Prediction: Read train and test data complete")
            logging.info(f'Parkinsons Disease Prediction: Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Parkinsons Disease Prediction: Test Dataframe Head : \n{test_df.head().to_string()}')
            
            target_column_name = 'status'
            drop_columns = [target_column_name]

            selected_columns = ["MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "RPDE", "DFA", "spread2", "D2"]
            x_train = train_df.loc[:, selected_columns]
            y_train=train_df[target_column_name]  

            x_test=test_df.loc[:, selected_columns]
            y_test=test_df[target_column_name]
            logging.info("Parkinsons Disease Prediction: Data Transformation completed successfully")
            
            return (x_train,y_train,x_test,y_test)
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise customexception(e,sys)