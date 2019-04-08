from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

# 클래스 기반 뷰 (Class-based View)
# 북마크 목록 출력
class BookmarkListView(ListView):
    model = Bookmark # 리스트에 사용할 모델(테이블) 지정
    paginate_by = 5 # 한 페이지에 출력할 오브젝트 수 지정

# 북마크 추가
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url'] # 입력받을 필드 설정
    success_url = reverse_lazy('list') # 입력 후 이동할 페이지 지정
    template_name_suffix = '_create' # bookmark_create 으로 템플릿 파일이름 지정

# 북마크 상세 페이지
class BookmarkDetailView(DetailView):
    model = Bookmark

# 북마크 내용 변경
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

# 북마크 삭제
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')