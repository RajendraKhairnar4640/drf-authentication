from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import (
    BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
class EmployeeView(APIView):
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self,request,pk=None, format=None):

        if pk is not None:
            emp = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self,requet,pk,format=None):
        
        emp = Employee.objects.get(pk=pk)
        emp.delete()
        return Response({'message':'employee deleted'})