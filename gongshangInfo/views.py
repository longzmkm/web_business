from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import companySerializers
from .models import company
# Create your views here.

# dataname='back'
# coll=collection()
# db=coll[dataname]
# employees=db['creditpub_2']


class CompanyListView(APIView):
    def get(self,request,format=None):
        #companyList=company.objects.filter(company_name=request.data.get('company_name'))
        # companyList=company.objects.all()
        if not  request.GET.get('company'):
            companyList=company.objects.all()
            serializer=companySerializers(companyList,many=True)
            return Response(serializer.data)
        else:
            companyList=company.objects.filter(company_name=request.GET.get('company'))
            serializer=companySerializers(companyList,many=True)
            return Response(serializer.data)
    def post(self,request,format=None):
        serializer = companySerializers(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETS'])
def company_detail(request,pk):
    try:
        company_item=company.objects.get(pk=pk)
    except company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        company_items=company.objects.filter(id=request.GET.get('pk'))
        serializer=companySerializers(company_item)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=companySerializers(company,request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


