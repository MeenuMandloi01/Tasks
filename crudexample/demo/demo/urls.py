from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
]
