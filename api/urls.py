from django.urls import include, path
from rest_framework import routers
from .views import ToDoViewSet


router = routers.DefaultRouter()
router.register(r'tasks', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]