from django.urls import include, path
from rest_framework import routers
from .views import ToDoViewSet,UsersViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'tasks', ToDoViewSet)
router.register(r'users', UsersViewSet)
  
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]