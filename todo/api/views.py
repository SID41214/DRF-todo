from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from api.serializers import RegisterSerializer
from rest_framework import response,status
# Create your views here.
class RegisterAPIView(GenericAPIView):
    serializer_class=RegisterSerializer
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    