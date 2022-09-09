from django import forms
from .models import app1

class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'