from app1.models import Generate_timesheet
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Generate_timesheet
        fields = ['Date', 'Day', 'Total hours', 'Particular']

