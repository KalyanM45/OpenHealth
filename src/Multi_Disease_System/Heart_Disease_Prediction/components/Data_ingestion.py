import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from src.logger import logging
from dataclasses import dataclass
from src.exception import customexception
from sklearn.model_selection import train_test_split

class DataIngestionConfig:
    raw_data_path:str   = os.path.join("Artifacts","Heart_Disease","Raw_data.csv")
    train_data_path:str = os.path.join("Artifacts","Heart_Disease","Train_data.csv")
    test_data_path:str  = os.path.join("Artifacts","Heart_Disease","Test_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Heart Disease Prediction: Data ingestion phase started")
        try:
            data = pd.read_csv("Notebook_Experiments\Data\heart.csv")
            logging.info("Heart Disease Prediction: Read the Data from the csv file")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Heart Disease Prediction: Created the raw data file")

            logging.info("Heart Disease Prediction: Splitting the data into train and test")
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            logging.info("Heart Disease Prediction: Data Splitting is done")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Heart Disease Prediction: Created the train and test data files")
            logging.info("Heart Disease Prediction: Data ingestion completed")

            return (self.ingestion_config.test_data_path,self.ingestion_config.train_data_path)
        
        except Exception as e:
            logging.info("Excpetion occured while ingesting the data")
            raise customexception(e,sys)