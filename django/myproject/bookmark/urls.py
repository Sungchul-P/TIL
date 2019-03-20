from django.urls import path
from . import views

app_name = "bookmark"

urlpatterns = [
    path('', views.BookmarkLV.as_view(), name="list"),
    # <pk> (Primary Key)는 정해진 값이므로 형식을 지켜줘야 한다.
    path('<pk>/', views.BookmarkDV.as_view(), name="detail"),
]
