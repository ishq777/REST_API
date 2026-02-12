
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    #web application endpoint
    path('students/', include('students.urls')),
    path('employees/', include('employees.urls')),
    path('blogs/', include('blogs.urls')),

    #API endpoints
    path('api/v1/', include('api.urls')),
]
