from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .model import BitcoinConversion,Query,Faq
from .serializers import BitcoinConverstion_serializer,Faq_serializer

class BitcoinConversionAPI(APIView):
    def get(self,request):
        serialized=BitcoinConverstion_serializer(BitcoinConversion.objects.all(),many=True)
        return Response({
            'detail':'success',
            'data':serialized.data
        })

class ContactQueryAPI(APIView):
    def post(self,request):
        data=request.data
        instance=Query(name=data['name'],email=data['email'],message=data['message'])
        instance.save()
        return Response({
            'detail':'success',
            'data':'successfully got the query'
        })

class FAQAPI(APIView):
    def get(self,request):
        all_faq=Faq.objects.all()
        serialized=Faq_serializer(all_faq,many=True)
        print(serialized.data)
        return Response({
            'detail':'success',
            'data':serialized.data
        })