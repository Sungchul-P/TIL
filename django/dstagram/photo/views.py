from django.shortcuts import render
from .models import Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# 사진 목록(함수형 뷰로 생성)
@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request,'photo/list.html', {'photos':photos})

# 사진 업로드
class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        # 작성자는 현재 로그인 한 사용자로 설정
        form.instance.author_id = self.request.user.id

        # 입력된 값들을 검증
        if form.is_valid():
            # 이상 없는 경우 DB에 저장하고, redirect 메서드로 메인페이지 이동
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

# 사진 삭제
class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

# 사진 수정
class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'

# 사진 상세 정보
class PhotoDetailView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/detail.html'