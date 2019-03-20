from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    # ForeignKey : 일대다(1:N) 관계로 연결하기.
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    # ManyToManyField : 다대다(M:N) 관계로 연결하기.
    # 여러 개의 Article이 여러 개의 Publication과 연결된다.
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('-headline',)

## 1:1 관계 예제 ##
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return '식당의 주소는 {} 입니다.'.format(self.address)

class Restaurant(models.Model):
    place = models.OneToOneField(Place, 
            on_delete=models.CASCADE, primary_key=True)

    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return '식당의 이름은 {}'.format(self.place.name)

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant,
            on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}, 직원은 {}".format(self.restaurant, self.name)

class Profile(models.Model):
    ## User 정보를 참조하는 방법 ##
    # 방법 1 #
    # from django.contrib.auth.models import User
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 방법 2 #
    # myproject/settings.py에 상수(AUTH_USER_MODEL='auth.User') 추가
    # from django.conf import settings
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

class Post(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                on_delete=models.CASCADE,
                related_name='modeltest_post_set')

    title = models.CharField(verbose_name="제목", max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True) # 최초 생성 날짜 저장
    updated_at = models.DateTimeField(auto_now=True) # 갱신 날짜 및 시간 저장
