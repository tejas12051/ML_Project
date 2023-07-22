import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)   #set the path for log file
os.makedirs(logs_path,exist_ok=True)   #It says even though there is file keep updating that folder,file

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

#for saving the file
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO  # info is used to pring the messages

)

