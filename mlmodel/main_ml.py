from .model_fetching import model_fetching
from .predict_next_10_day import predict_next
from .model_fitting import fit_my_model
from .data_fetching import fetch_save_prev_and_new_except_prev
from .utils import save_file
import pandas as pd  
import os
import datetime

from .graph_generator import make_future_graph

def make_future_prediction():
    time_step=10
    previous_data,new_data_except_prev=fetch_save_prev_and_new_except_prev()
    model,input_transformer,output_transformer=model_fetching()
    if(new_data_except_prev.shape[0]!=0):
        fitted_model,fitted_input_transformer,fitted_output_transformer=fit_my_model(
                model=model,
                input_transformer=input_transformer,
                output_transformer=output_transformer,
                data=pd.concat((previous_data.iloc[-time_step:,],new_data_except_prev))
            )
        whole_data=pd.read_csv(os.path.join('mlmodel','artifacts','preprocessed_bitcoin1.csv'))
        future_10=predict_next(
                next_day=10,
                model=fitted_model,
                previous_10_day_data=whole_data.iloc[-time_step:,],
                input_transformer=input_transformer,
                output_transformer=output_transformer
            )
    else:
        fitted_model,fitted_input_transformer,fitted_output_transformer=model,input_transformer,output_transformer
        future_10=pd.read_csv(os.path.join('mlmodel','artifacts','future10.csv'))
    print(future_10)
    today=datetime.datetime.now()
    save_file(path=os.path.join('mlmodel','model_pkl','model',f'my_model{today.day+today.hour+today.minute}.pkl'),obj=fitted_model)
    save_file(path=os.path.join('mlmodel','model_pkl','input_transformer',f'input_transformer{today.day+today.hour+today.minute}.pkl'),obj=fitted_input_transformer)
    save_file(path=os.path.join('mlmodel','model_pkl','output_transformer',f'output_transformer{today.day+today.hour+today.minute}.pkl'),obj=fitted_output_transformer)
    future_10.to_csv('mlmodel/artifacts/future10.csv',index=False)
    return future_10

if __name__=='__main__':
        df=pd.read_csv(os.path.join('mlmodel','artifacts','preprocessed_bitcoin1.csv'))
        make_future_prediction()
        future_df=pd.read_csv('mlmodel/artifacts/future10.csv')
        make_future_graph(future_df)