from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls, name='admin-page'),
    path('employee/', include('employees.urls')),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),

]
