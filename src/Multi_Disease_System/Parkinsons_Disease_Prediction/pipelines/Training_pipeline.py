from src.Multi_Disease_System.Parkinsons_Disease_Prediction.components.Data_ingestion import DataIngestion
obj=DataIngestion()
train_data_path,test_data_path=obj.initiate_data_ingestion()


from src.Multi_Disease_System.Parkinsons_Disease_Prediction.components.Data_transformation import DataTransformation
data_transformation=DataTransformation()
x_train, x_test, y_train, y_test=data_transformation.initialize_data_transformation(train_data_path,test_data_path)

#from src.Multi_Disease_System.Parkinsons_Disease_Prediction.components.Model_trainer import ModelTrainer
#model_trainer_obj=ModelTrainer()
#model_trainer_obj.initiate_model_training(x_train, x_test, y_train, y_test)