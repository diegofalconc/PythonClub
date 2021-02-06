from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resource'),
    path('meeting/<int:id>', views.meeting, name ='detail')
]
