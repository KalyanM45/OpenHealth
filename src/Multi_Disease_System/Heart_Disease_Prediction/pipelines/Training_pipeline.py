from src.Multi_Disease_System.Heart_Disease_Prediction.components.Data_ingestion import DataIngestion
from src.Multi_Disease_System.Heart_Disease_Prediction.components.Data_transformation import DataTransformation
from src.Multi_Disease_System.Heart_Disease_Prediction.components.Model_trainer import ModelTrainer
from src.Multi_Disease_System.Heart_Disease_Prediction.components.Model_evaluation import ModelEvaluation

class Heart_Disease:

    def train_heart(self):
        obj=DataIngestion()
        train_data_path,test_data_path=obj.initiate_data_ingestion()

        data_transformation=DataTransformation()
        x_train, x_test, y_train, y_test=data_transformation.initialize_data_transformation(train_data_path,test_data_path)

        model_trainer_obj=ModelTrainer()
        model_trainer_obj.initiate_model_training(x_train, x_test, y_train, y_test)

        model_eval_obj = ModelEvaluation()
        model_eval_obj.initate_model_evaluation(x_train, x_test, y_train, y_test)