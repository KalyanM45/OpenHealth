import os
import sys
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from xgboost import XGBClassifier
from dataclasses import dataclass
from src.logger import logging
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from src.exception import customexception
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from src.utils import save_object, evaluate_model
from sklearn.model_selection import GridSearchCV



@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('Artifacts','Heart_Disease','Heart_Model.pkl')
    
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, x_train, x_test, y_train, y_test):
        print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
        try:
            
            models = {
                'Logistic Regression': LogisticRegression(),
                'Naive Bayes': GaussianNB(),
                'Random Forest Classifier': RandomForestClassifier(),
                'XG Boost': XGBClassifier(),
                'K Nearest Neighbors': KNeighborsClassifier(),
                'Decision Tree': DecisionTreeClassifier(),
                'Support Vector Machine': SVC()
            }

            param_grid = {
                'Random Forest Classifier': {'n_estimators': [10, 20, 30], 'max_depth': [5, 10, 15]},
                'XG Boost': {'learning_rate': [0.01, 0.1, 0.2], 'max_depth': [10, 15, 20], 'subsample': [0.5, 0.7, 0.9]},
                'K Nearest Neighbors': {'n_neighbors': [5, 10, 15]},
                'Decision Tree': {'max_depth': [4, 6, 8], 'criterion': ['gini', 'entropy']},
                'Support Vector Machine': {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
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