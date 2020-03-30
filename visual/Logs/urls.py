from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Jogs/',include('Jobs.urls')),
    path('Logs/',include('Logs.urls')),
]
