from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

class BookmarkLV(ListView):
    # 데이터가 object_list에 들어있다는 전제하에 사용
    model = Bookmark 

class BookmarkDV(DetailView):
    # 데이터가 object에 들어있다는 전제하에 사용
    model = Bookmark 