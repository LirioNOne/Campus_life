from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CampusLife.urls', namespace='main')),
    path('', include('registration.urls', namespace='registration')),
]
