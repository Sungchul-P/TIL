from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    # 목록에 보일 필드를 설정
    list_display = ['id','author','created','updated']
    
    # ForeignKey 필드를 값을 써넣는 형태로 바꾸고 검색 기능을 사용해 선택할 수 있게 한다.
    raw_id_fields = ['author']
    
    # 필터 기능을 사용할 필드를 선택(ForeignKey 필드는 설정 불가)
    list_filter = ['created','updated','author']

    # 검색 기능을 통해 검색할 필드를 선택
    search_fields = ['text','created']

    # 관리자 사이트에서 기본으로 사용할 정렬값을 설정
    ordering = ['-updated','-created']

admin.site.register(Photo, PhotoAdmin)