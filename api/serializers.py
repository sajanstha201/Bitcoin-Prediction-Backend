from rest_framework import serializers
from .model import BitcoinConversion,Faq
class BitcoinConverstion_serializer(serializers.ModelSerializer):
    class Meta:
        model=BitcoinConversion
        fields='__all__'
        
class Faq_serializer(serializers.ModelSerializer):
    class Meta:
        model=Faq
        fields='__all__' 
