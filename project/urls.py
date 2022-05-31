from django.urls import path
from .import views

urlpatterns = [
    path('',views.homePage,name='homePage'),
    path('addtasks',views.addProject,name='addtasks'),
    path('viewtasks/',views.displayTask,name='viewtasks'),
    path('deletetasks/<str:pk>',views.deleteTask,name='deletetasks'),
    path('updatetasks/<str:pk>',views.updateTask,name='updatetasks'),
    path('updatestatus/<str:pk>',views.updateStatus,name='updatestatus'),
]