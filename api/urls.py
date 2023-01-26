from django.urls import include, path
from rest_framework import routers
from .views import ToDoViewSet,UsersViewSet


router = routers.DefaultRouter()
router.register(r'tasks', ToDoViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]