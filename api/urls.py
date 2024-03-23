from django.urls import path
from .views import BitcoinConversionAPI,ContactQueryAPI,FAQAPI
from mlmodel.views import FutureGraphAPI
urlpatterns = [
    path('bitcoinrate/',BitcoinConversionAPI.as_view(),name="bitcoinrate_url"),
    path('post-query/',ContactQueryAPI.as_view()),
    path('graph-authenticated/',FutureGraphAPI.as_view()),
    path('faq/',FAQAPI.as_view(),name='faq_url')
]
