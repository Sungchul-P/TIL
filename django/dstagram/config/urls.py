from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')), # photo앱을 메인 페이지로 동작시킴
    path('accounts/', include('accounts.urls')),
]

# static을 사용해서 MEDIA_URL에 해당하는 주소를 가진 요청에 대해서는
# MEDIA_ROOT에서 찾아서 응답하도록 urlpatterns에 추가한다.
# Debug=True 일때만 이 구문은 동작한다.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)