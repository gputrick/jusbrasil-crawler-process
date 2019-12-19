from django.urls import include, path
from rest_framework import routers
from processsearch import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'processes', views.ProcessViewSet)
ROUTER.register(r'move', views.MoveViewSet)

urlpatterns = [
    path('', include(ROUTER.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url('^processes/(?P<process_number>.+)/$', views.CrawlerProcess.as_view()),
]