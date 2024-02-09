import os
import sys
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from xgboost import XGBClassifier
from dataclasses import dataclass
from src.logger import logging
from sklearn.metrics import accuracy_score
from src.utils import save_object, evaluate_model

from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier



@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('Artifacts','Parkinsons_Disease','Parkinsonss_Model.pkl')
    
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, x_train, x_test, y_train, y_test):
        try:
            
            models = {
                'LR': LogisticRegression(),
                'NB': GaussianNB(),
                'XGB': XGBClassifier(learning_rate=0.01, n_estimators=25, max_depth=15, gamma=0.6, subsample=0.52, 
                                     colsample_bytree=0.6, seed=27,reg_lambda=2, booster='dart', colsample_bylevel=0.6,
                                     colsample_bynode=0.5),
                'RF': RandomForestClassifier(),
                'GB': GradientBoostingClassifier(),
                'DT': DecisionTreeClassifier(criterion='entropy', random_state=0, max_depth=6),
                'KNN': KNeighborsClassifier(),
                'EXT': ExtraTreesClassifier()
            }

            model_report:dict=evaluate_model(x_train,y_train,x_test,y_test,models)

            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            logging.info('Exception occurred at Model Training')
            raise customexception(e, sys)