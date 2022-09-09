from django.urls import path
from . import views


urlpatterns = [
    path('get_detail/', views.generate_monthly_work_report, name="monthly_report"),
    path('data/', views.user),
]