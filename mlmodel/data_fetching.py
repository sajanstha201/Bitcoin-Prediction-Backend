import pandas as pd
import numpy as np
import os
from pathlib import Path
import datetime
import time
BASE_DIR = Path(__file__).resolve().parent.parent
import os
def fetch_previous_data():
    df=pd.read_csv(os.path.join('mlmodel','artifacts','preprocessed_bitcoin1.csv'))
    return df

def fetch_data_from2020():
    ticker = 'BTC-USD'
    yesterday=datetime.datetime.now()-datetime.timedelta(days=2)
    period1 = int(time.mktime(datetime.datetime(2020, 1, 1, 23, 59).timetuple()))
    period2 = int(time.mktime(datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 23, 59).timetuple()))
    interval = '1d' # 1d, 1m
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    df = pd.read_csv(query_string)
    return df

def fetch_data_except_prev():
    previous_data=fetch_previous_data()
    recent_data=fetch_data_from2020()
    new_data=recent_data[recent_data[recent_data['Date']==previous_data.iloc[-1,]['Date']].index.values[0]:]
    new_data.drop('Adj Close',axis=1,inplace=True)
    new_data.rename(columns={'Volume':'Capital'},inplace=True)
    new_data['volume']=round(new_data['Capital']/(new_data['Open']+new_data['Close']+new_data['High']+new_data['Low'])*4)
    new_data['price_change'] = np.where(new_data['Open'] != 0.0, ((new_data['Close'] - new_data['Open']) / new_data['Open'] * 100), 10)
    x=list(new_data['Capital'])
    y=[ (x[i]-x[i-1])/x[i-1]*100 for i in range(1,new_data.shape[0])]
    y.insert(0,0)
    new_data['capital_change']=y
    feature=['Date','Open','High','Low','Close','Capital','price_change','volume','capital_change']
    return new_data.iloc[1:,][feature]

def save_merge_prev_new(new,previous):
    merged=pd.concat((previous,new))
    path=os.path.join('mlmodel','artifacts','preprocessed_bitcoin1.csv')
    merged.to_csv(path,index=False)
    return merged

def fetch_save_prev_and_new_except_prev():
    prev=fetch_previous_data()
    new=fetch_data_except_prev()
    save_merge_prev_new(new=new,previous=prev)
    return prev,new

def fetch_save_new_data():
    prev=fetch_previous_data()
    new=fetch_data_except_prev()
    save_merge_prev_new(new=new,previous=prev)
    return new



if __name__=='__main__':
    new=fetch_save_new_data()