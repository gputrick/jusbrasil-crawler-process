from django.urls import include, path
from rest_framework import routers
from processsearch import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'processes', views.ProcessViewSet)

urlpatterns = [
    path('', include(ROUTER.urls)),
]