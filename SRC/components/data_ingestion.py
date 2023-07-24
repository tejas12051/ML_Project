import os
import sys
from SRC.exception import CustomException
from SRC.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from SRC.components.data_transformation import DataTransformation
from SRC.components.data_transformation import DataTransformationConfig



# This is the i/p which we are giving to Data Ingestion components.
# Now Data Ingestion knows where to save the train and test path.
@dataclass
class DataingestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataingestionConfig()  #If we call this class, the three paths will be saved in this ingestion_config variable    

    def initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion method or componenet")

        try:
            # To read the data. eg. mongoDB, S3, Api
            df = pd.read_csv('notebook/data/stud.csv')      ## Here you can change the code and read it from anywhere else
            logging.info("Read the dataset as dataframe")

            ## We know the train,test file path now make the folder with the help of train,test and raw data 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)  # exist_ok=True : If folder is there we keep it that folder and we dont have to delete and update it again

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)  # Raw data path is saved

            logging.info("Train Test Split initiated")

            train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)

            # we are saving the train_set and test_set in Artifacts folder
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")

            ## We are returning the train and test path, to grab this data for next step like data transformation
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
            

if __name__=="__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)