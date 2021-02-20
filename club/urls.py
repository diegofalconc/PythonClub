from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resource'),
    path('meeting/', views.meeting, name ='meeting'),
    path('meetingdetail/<int:id>', views.meetingDetail, name='detail'),
]
