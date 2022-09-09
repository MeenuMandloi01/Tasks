from django import forms
from app1.models import Student


class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"