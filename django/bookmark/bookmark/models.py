from django.db import models

# 테이블 및 변수(컬럼) 설정
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        # 객체를 호출할 때 출력할 내용
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    # 북마크 수정 후, 이동할 페이지 지정
    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
    