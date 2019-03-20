from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import reverse

class Post(models.Model):

    # name = models.TextField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                on_delete=models.CASCADE,
                related_name='shop_post_set')

    title = models.CharField(verbose_name="제목", max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True) # 최초 생성 날짜 저장
    updated_at = models.DateTimeField(auto_now=True) # 갱신 날짜 및 시간 저장

STATUS_CHOICES = (
('d', 'Draft'),
('p', 'Published'),
('w', 'Withdrawn'),
)

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    def __str__(self):
        return self.title

    def get_absolute_url2(self):
        return reverse('shop:detail', args=[self.id])

    class Meta:
        ordering=['-id']

    # success_url이 없으면 자동 호출된다.
    def get_absolute_url(self):
        return reverse("shop:detail", kwargs={"pk": self.id})
    