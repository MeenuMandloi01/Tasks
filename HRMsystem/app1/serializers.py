from rest_framework import serializers
from app1.models import Employee, HRregistration
from django.db.models import fields
from django.contrib.auth.models import User


class HRregistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRregistration
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_name', 'email', 'password')


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('mobile', 'address', 'designation', 'department')


class EmpAllSerializer(serializers.Serializer):
    class Meta:
        model = Employee
        fields = '__all__'
