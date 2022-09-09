from django.contrib import admin
from django.urls import path, include
#DataFlair
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls'))
]