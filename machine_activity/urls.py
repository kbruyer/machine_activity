from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MA_login/', include('MA_login.urls')),
    path('MA_main/', include('MA_main.urls')),
    path('', include('MA_main.urls')),
]
