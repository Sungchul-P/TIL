from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('', views.book_list, name="list"),
    path('<pk>/detail/', views.book_detail, name="detail"),
    path('<pk>/edit/', views.book_edit, name="edit"),
    path('<pk>/delete/', views.book_delete, name="delete"),
    path('new/', views.book_new, name="new"),

]
