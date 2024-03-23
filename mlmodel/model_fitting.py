
import numpy as np

def fit_my_model(model,input_transformer,output_transformer,data):
    time_step=10
    input_feature=['Open','High','Low','Close','Capital','price_change','volume','capital_change']
    output_feature=['Open','High','Low','Close','Capital','volume']
    input_transformer.fit(data[input_feature])
    output_transformer.fit(data[output_feature])
    x=input_transformer.transform(data[input_feature])
    y=output_transformer.transform(data[output_feature])
    x_train=create_time_step(x)
    y_train=y[time_step:]
    print(np.array(x).shape,np.array(y).shape)
    print(np.array(x_train).shape,np.array(y_train).shape)
    while(1):
        history=model.fit(x_train,y_train,batch_size=32,epochs=100)
        if(history.history['mean_absolute_error'][99]<0.2):
            break
    return model,input_transformer,output_transformer

def create_time_step(x):
    time_step=10
    x_step=[]
    for i in range(time_step,x.shape[0]):
        x_step.append(x[i-time_step:i])
    return np.array(x_step)