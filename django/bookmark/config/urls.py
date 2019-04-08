from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', include('bookmark.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('admin/', admin.site.urls),
]
