
from django.contrib import admin
from django.urls import path, include
from login import views as login_views
from employees import views as employees_views

urlpatterns = [

    path('', employees_views.home, name='homepage'),
    path('add/',employees_views.add, name ='add'),
    path('admin/', admin.site.urls, name='admin-page'),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),
    path('profile/', login_views.user_profile, name='profile'),
    path('logout/', login_views.user_logout, name='logout'),
    path('task-detail/<int:employee_id>', employees_views.task_detail, name='task_detail'),
    path('search/', employees_views.search, name='search')
]
