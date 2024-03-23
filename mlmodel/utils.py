import os
import dill
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
import keras
BASE_DIR = Path(__file__).resolve().parent.parent

def load_file(path):
    try:
        with open(path,'rb') as file:
            loaded_file=pickle.load(file)
            return loaded_file
    except Exception as e:
        print("THIS IS THE ERROR MESSAGE WHILE LOADING THE FILE\n")
        print(e)
        return False  
    
def save_file(path,obj):
    try:
        with open(path,'wb') as file:
            pickle.dump(obj,file)
            return True
    except Exception as e:
        print("THIS IS THE ERROR MESSSGE WHILE SAVING THE FILE\n")
        print(e)
        return False