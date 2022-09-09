from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app1 import views

urlpatterns = [
    path('hr_regist/', views.HRregistrationList.as_view()),
    path('regist/', views.RegistrationList.as_view()),
    path('registered/<int:pk>/', views.RegistrationDetails.as_view()),
    path('emp_detail/<int:pk>/', views.EmpDetails.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
