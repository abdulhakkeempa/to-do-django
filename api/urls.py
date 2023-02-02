from django.urls import include, path,re_path
from rest_framework import routers
from .views import ToDoViewSet,UsersViewSet,UserCreateAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
# router.register(r'tasks', ToDoViewSet)
router.register(r'users', UsersViewSet)
  
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',UserCreateAPI.as_view()),
    path('tasks/',ToDoViewSet.as_view()),
    path('tasks/<str:pk>',ToDoViewSet.get_object)
]