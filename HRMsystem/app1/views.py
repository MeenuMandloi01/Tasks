from django.shortcuts import render
from app1.models import Employee
from app1.serializers import RegistrationSerializer, EmployeeDetailSerializer, EmpAllSerializer, \
    HRregistrationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import AllowAny


class HRregistrationList(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = HRregistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def login(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegistrationList(APIView):
    def get(self, request):
        reg_user = Employee.objects.all()
        serializer = RegistrationSerializer(reg_user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationDetails(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reg_user = self.get_object(pk)
        serializer = RegistrationSerializer(reg_user)
        return Response(serializer.data)

    def put(self, request, pk):
        reg_user = self.get_object(pk)
        serializer = RegistrationSerializer(reg_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpDetails(APIView):
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reg_user = self.get_object(pk)
        print("data : ", reg_user)
        serializer = EmpAllSerializer(reg_user)
        return Response(serializer.data)

    def put(self, request, pk):
        reg_user = self.get_object(pk)
        serializer = EmployeeDetailSerializer(reg_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("data: ", serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
