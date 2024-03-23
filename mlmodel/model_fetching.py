from .utils import load_file
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import os
def model_fetching():
    input_transformer=load_file(os.path.join('mlmodel','model_pkl','input_transformer.pkl'))
    output_transformer=load_file(os.path.join('mlmodel','model_pkl','output_transformer.pkl'))
    model=load_file(os.path.join('mlmodel','model_pkl','my_model.pkl'))
    return model,input_transformer,output_transformer