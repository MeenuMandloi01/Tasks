from django.shortcuts import render
from app1.forms import StuForm


def index(request):
    stu = EmpForm()
    return render(request, "image.html", {'forms': stu})