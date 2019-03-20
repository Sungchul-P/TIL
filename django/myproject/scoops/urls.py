from django.urls import path, re_path, register_converter
from django.conf.urls import url
from .myconverters import CodeConverter
from . import views

app_name = "scoops"

# Converter 등록
register_converter(CodeConverter, "mycode")

urlpatterns = [
    path('', views.index, name="index"),
    # url(r'(?P<word>[0-9a-zA-Z]{4})/$', views.test1),
    # url(r'(?P<word>\w{4})/$', views.test1, name="my1"),
    # re_path(r'(?P<word>[0-9a-zA-Z]{4})/$', views.test2),
    # url(r'(?P<word>[0-9a-zA-Z]{4})/(?P<second>[0-9a-zA-Z]{2})/$', views.test3),
    re_path(r'(?P<word>\w{4})/(?P<second>\w{2})/$', views.test4, name="my4"),

    # Path Converter 이용해서 패턴 정의
    path('article/<int:year>/<int:month>/<slug:myname>', views.test6),

    # 사용자 정의 Converter 이용
    path('article/<mycode:num>/', views.func7),
]
