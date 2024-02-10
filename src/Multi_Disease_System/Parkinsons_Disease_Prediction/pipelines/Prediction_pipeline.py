import os
import sys
import pandas as pd
from src.logger import logging
from src.utils import load_object
from src.exception import customexception

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            model_path=os.path.join("Artifacts","Parkinsons_Disease","Parkinsons_Model.pkl")
            model=load_object(model_path)
            pred=model.predict(features)
            return pred
        except Exception as e:
            raise customexception(e,sys)
    
class CustomData:
    def __init__(self,
                 MDVPFO:float,
                 MDVPFHI:float,
                 MDVPFLO:float,
                 MDVPJ:float,
                 RPDE:float,
                 DFA:float,
                 spread2:float,
                 D2:float):
        
        self.MDVPFO = MDVPFO
        self.MDVPFHI = MDVPFLO
        self.MDVPFLO = MDVPFLO
        self.MDVPJ = MDVPJ
        self.RPDE = RPDE
        self.DFA = DFA
        self.spread2 = spread2
        self.D2 = D2
            
                
    def get_data_as_dataframe(self):
            try:
                custom_data_input_dict = {
                    'MDVPFO':[self.MDVPFO],
                    'MDVPFHI':[self.MDVPFHI],
                    'MDVPFLO':[self.MDVPFLO],
                    'MDVPJ':[self.MDVPJ],
                    'RPDE':[self.RPDE],
                    'DFA':[self.DFA],
                    'spread2':[self.spread2],
                    'D2':[self.D2]
                }
                df = pd.DataFrame(custom_data_input_dict)
                print(df)
                logging.info('Dataframe Gathered')
                return df
            except Exception as e:
                logging.info('Exception Occured in prediction pipeline')
                raise customexception(e,sys)
