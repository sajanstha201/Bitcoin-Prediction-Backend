from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
import pandas as pd
import os
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .main_ml import make_future_prediction
from .graph_generator import make_graph,make_future_graph
import datetime
import base64
class FutureGraphAPI(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        now=datetime.datetime.now()
        today=datetime.datetime(now.year,now.month,now.day)
        today
        df=pd.read_csv(os.path.join('mlmodel','artifacts','preprocessed_bitcoin1.csv'))
        if((datetime.datetime.strptime(df.iloc[-1]['Date'],'%Y-%m-%d'))<today-datetime.timedelta(days=1)):
            print("sajan shrestha")
            make_future_prediction()
            future_df=pd.read_csv('mlmodel/artifacts/future10.csv')
            make_future_graph(future_df)
            
        with open(os.path.join('mlmodel','media','bitcoin_future10_graph.png'),'rb') as file:
            graph=file.read()
        with open(os.path.join('mlmodel','media','bitcoin_future10_table.png'),'rb') as file:
            table=file.read()
        image_graph = base64.b64encode(graph).decode('utf-8')
        image_table=base64.b64encode(table).decode('utf-8')
        json_data=[{'name':'GRAPH','data':image_graph},{'name':'TABLE','data':image_table}]
        return JsonResponse(json_data,safe=False)

def graph(request):
    df=pd.read_csv(os.path.join('mlmodel','artifacts','preprocessed_bitcoin1.csv'))
    now=datetime.datetime.now()
    today=datetime.datetime(now.year,now.month,now.day)
    if(datetime.datetime.strptime(df.iloc[-1]['Date'],'%Y-%m-%d')<today-datetime.timedelta(days=1)):
        make_future_prediction()
        updated_df=pd.read_csv(os.path.join('mlmodel','artifacts','preprocessed_bitcoin1.csv'))
        make_graph(updated_df) 
    return render(request,'graph.html')