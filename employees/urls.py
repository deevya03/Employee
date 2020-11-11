from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('add/', views.add, name='add'),
    path('search/', views.search, name='search'),
    path('task-detail/<int:employee_id>', views.task_detail, name='task_detail'),
]
