
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',include('MyApp1.urls')),
    path('second/',include('MyApp2.urls')),
    path('third/',include('MyApp3.urls')),
]


