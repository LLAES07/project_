import os 
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomExecption
import dill

def save_object(file_path, obj):

    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomExecption(e, sys)