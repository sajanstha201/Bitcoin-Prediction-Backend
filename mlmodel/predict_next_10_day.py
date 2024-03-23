
import numpy as np
import pandas as pd  
import datetime
def predict_next(next_day,model,previous_10_day_data,input_transformer,output_transformer):
    data_test=previous_10_day_data
    feature=['Date','Open','High','Low','Close','Capital','price_change','volume','capital_change']
    input_feature=['Open','High','Low','Close','Capital','price_change','volume','capital_change']
    target_feature=['Open','High','Low','Close','Capital','volume']
    x_f={}
    x=[]
    x.append(list(data_test[input_feature].iloc[-1,]))
    time_step=10
    first_data=np.array(input_transformer.transform(data_test.iloc[-time_step:,1:]))
    x_f=pd.DataFrame(x_f)
    for i in range(len(input_feature)):
        x_f[input_feature[i]]=first_data[:,i]
    for i in range(next_day):
        pred=model.predict(np.array(x_f.iloc[-time_step:,]).reshape(1,time_step,-1))
        pred_value=np.array(output_transformer.inverse_transform(pred)).reshape(-1)
        y=list(pred_value)
        y.insert(5,(pred_value[3]-pred_value[0])/pred_value[0]*100)
        y.append((pred_value[4]-x[-1][4])/x[-1][4]*100)
        x.append(y)
        x_={}
        for i in range(len(input_feature)):
            x_[input_feature[i]]=[y[i]]
        x_=pd.DataFrame(x_)
        x_f.loc[time_step+i]=np.array(input_transformer.transform(x_)).reshape(-1)
    df={}
    x=np.array(x)
    for i in range(len(input_feature)):
        df[input_feature[i]]=x[:,i]
    final_prediction=pd.DataFrame(df)
    today_date=datetime.datetime.strptime(previous_10_day_data.iloc[-1]['Date'],'%Y-%m-%d')
    time_list=[]
    for i in range(next_day+1):
        time_list.append(today_date+datetime.timedelta(days=i*1))
    final_prediction['Date']=time_list
    return final_prediction[feature].iloc[1:,]
