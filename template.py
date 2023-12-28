import os
from pathlib import Path

list_of_files = [
    ".github/workflows/main.yaml",

    "Notebook_Experiments/Data/.gitkeep",
    "Notebook_Experiments/Heart_Disease_Prediction.ipynb",
    "Notebook_Experiments/Diabetes_Disease_Prediction.ipynb",
    "Notebook_Experiments/Breast_Cancer_Prediction.ipynb",
    "Notebook_Experiments/Skin_Cancer_Prediction.ipynb",
    "Notebook_Experiments/Parkinsons_Disease_Prediction.ipynb",
    "Notebook_Experiments/Brain_Tumor_Detection.ipynb",
    "Notebook_Experiments/Lung_Disease_Prediction.ipynb",
    "Notebook_Experiments/Kidney_Disease_Prediction.ipynb",
    "Notebook_Experiments/Liver_Disease_Prediction.ipynb",
    "Notebook_Experiments/Pneumonia_Prediction.ipynb",
    "Notebook_Experiments/Malaria_Prediction.ipynb",
    "Notebook_Experiments/Ocular_Prediction.ipynb",

    "src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",

    "src/Multi_Disease_System/__init__.py",

    "src/Multi_Disease_System/Heart_Disease_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Heart_Disease_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Heart_Disease_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Heart_Disease_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Heart_Disease_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Heart_Disease_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Heart_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Heart_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Diabetes_Disease_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Diabetes_Disease_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Diabetes_Disease_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Diabetes_Disease_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Diabetes_Disease_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Diabetes_Disease_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Diabetes_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Diabetes_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Breast_Cancer_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Breast_Cancer_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Breast_Cancer_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Breast_Cancer_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Breast_Cancer_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Breast_Cancer_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Breast_Cancer_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Breast_Cancer_Prediction/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Skin_Cancer_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Skin_Cancer_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Skin_Cancer_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Skin_Cancer_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Skin_Cancer_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Skin_Cancer_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Skin_Cancer_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Skin_Cancer_Prediction/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Parkinsons_Disease_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Parkinsons_Disease_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Parkinsons_Disease_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Parkinsons_Disease_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Parkinsons_Disease_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Parkinsons_Disease_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Parkinsons_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Parkinsons_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Brain_Tumor_Detection/components/__init__.py",
    "src/Multi_Disease_System/Brain_Tumor_Detection/components/Data_ingestion.py",
    "src/Multi_Disease_System/Brain_Tumor_Detection/components/Data_transformation.py",
    "src/Multi_Disease_System/Brain_Tumor_Detection/components/Model_trainer.py",
    "src/Multi_Disease_System/Brain_Tumor_Detection/components/Model_evaluation.py",
    "src/Multi_Disease_System/Brain_Tumor_Detection/pipelines/__init__.py",
    "src/Multi_Disease_System/Brain_Tumor_Detection/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Brain_Tumor_Detection/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Lung_Disease_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Lung_Disease_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Lung_Disease_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Lung_Disease_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Lung_Disease_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Lung_Disease_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Lung_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Lung_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Kidney_Disease_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Kidney_Disease_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Kidney_Disease_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Kidney_Disease_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Kidney_Disease_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Kidney_Disease_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Kidney_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Kidney_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Liver_Disease_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Liver_Disease_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Liver_Disease_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Liver_Disease_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Liver_Disease_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Liver_Disease_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Liver_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Liver_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Pneumonia_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Pneumonia_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Pneumonia_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Pneumonia_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Pneumonia_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Pneumonia_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Pneumonia_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Pneumonia_Prediction/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Malaria_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Malaria_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Malaria_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Malaria_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Malaria_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Malaria_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Malaria_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Malaria_Prediction/pipelines/Training_pipeline.py",

    "src/Multi_Disease_System/Ocular_Prediction/components/__init__.py",
    "src/Multi_Disease_System/Ocular_Prediction/components/Data_ingestion.py",
    "src/Multi_Disease_System/Ocular_Prediction/components/Data_transformation.py",
    "src/Multi_Disease_System/Ocular_Prediction/components/Model_trainer.py",
    "src/Multi_Disease_System/Ocular_Prediction/components/Model_evaluation.py",
    "src/Multi_Disease_System/Ocular_Prediction/pipelines/__init__.py",
    "src/Multi_Disease_System/Ocular_Prediction/pipelines/Prediction_pipeline.py",
    "src/Multi_Disease_System/Ocular_Prediction/pipelines/Training_pipeline.py",

    "src/Diet_Recommendation/__init__.py",
    "src/Food_Recommendation/__init__.py",
    "src/Large_Language_Model/__init__.py",    

    "static/styles.css",
    "templates/index.html",
    "templates/result.html",
    ".gitignore",
    "app.py",
    "Dockerfile",
    "README.md",
    "dvc.yaml",
    "requirements.txt",
    "setup.py"]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass