from django.shortcuts import render

from .models import*
from .serializers import*
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class user_view(APIView):
    def get(self,request,id=None):  
        if id:
        
            try:
                uid=user.objects.get(id=id)
                serializer=user_serializer(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        else:
            uid=user.objects.all()
            serializer=user_serializer(uid,many=True)
            return Response({'status':'success','data':serializer.data})
      
    def post(self,request):
        serializer=user_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
     
    def patch(self,request,id=None):
        try:
            uid=user.objects.get(id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=user_serializer(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
        
          
        
        
        
    def delete(self,request,id=None):
        if id:
            try:
                uid=user.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        else:
            return Response({'status':"invalid data"})

        