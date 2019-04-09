from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    # author 필드를 ForeignKey로 User 테이블과의 관계를 만듭니다.
    # CASCADE : 연결된 객체가 지워지면 해당 하위 객체도 같이 삭제합니다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')

    # upload_to : 사진이 업로드 될 경로를 설정합니다. 업로드 실패 시 default 값으로 대체 합니다.
    # ImageField 를 사용하려면 "pillow" 모듈이 설치되어 있어야 합니다. (pip install pillow)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')

    # 사진에 대한 설명을 저장할 텍스트 필드입니다.
    text = models.TextField()

    # 글 작성 일을 저장하기 위한 날짜시간 필드입니다.
    # auto_now_add=True : 객체가 추가될 때 자동으로 값을 설정합니다.
    created = models.DateTimeField(auto_now_add=True)

    # 글 수정 일을 저장하기 위한 날짜시간 필드입니다.
    # auto_now=True : 객체가 수정될 때마다 자동으로 값을 설정합니다.
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        # 글 수정 시간을 기준으로 내림차순 정렬합니다.
        ordering = ['-updated']


    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    # 객체의 상세 페이지의 주소를 반환하는 메서드
    def get_absolute_url(self):
        # reverse() : URL 패턴 이름을 가지고 해당 패턴을 찾아 주소를 만들어 주는 함수
        return reverse("photo:photo_detail", args=[str(self.id)])
        