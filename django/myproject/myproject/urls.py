"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse, redirect
from django.conf import settings
from django.conf.urls.static import static

def root(request):
    return redirect('shop:list')
    # return HttpResponse("ROOT 입니다.(초기화면)")

# 앱의 urls을 등록한다.
urlpatterns = [
    # path('', root),
    path('', lambda r : redirect('shop:list')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('scoops/', include('scoops.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('shop/', include('shop.urls')),
    path('book/', include('book.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)