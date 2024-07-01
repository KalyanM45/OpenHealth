import os
import sys
import logging
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level = logging.INFO, 
                    filename = LOG_FILEPATH, 
                    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
        