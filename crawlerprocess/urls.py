from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('processsearch.urls')),
    path('admin/', admin.site.urls),
]