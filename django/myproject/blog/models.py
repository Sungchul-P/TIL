from django.db import models
from django.contrib.postgres.fields import JSONField
import datetime
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import User
from django.conf import settings

# 클래스 1개가 테이블 1개
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                on_delete=models.CASCADE,
                related_name='blog_post_set')

    title = models.CharField(verbose_name="제목", max_length=100)
    content = models.TextField()
    # tag_set = models.ManyToManyField('Tag')
    created_at = models.DateField(auto_now_add=True) # 최초 생성 날짜 저장
    updated_at = models.DateTimeField(auto_now=True) # 갱신 날짜 및 시간 저장

    def latlng_validation(value):
        check = re.match(r"(\d+\.?\d*),(\d+\.?\d*)", value)
        if not check:
            raise ValidationError("유효하지 않은 위도, 경도입니다.")

    lating = models.CharField(max_length=100, blank=True,
                    validators=[latlng_validation], help_text="위도와 경도를 입력하세요.")

    def validation_even(value):
        if value % 2 != 0:
            raise ValidationError(str(value) + "가 짝수이어야 한다.")

    even_field = models.IntegerField(validators=[validation_even])

    def __str__(self):
        return "title:{} || id:{}".format(self.title,str(self.id))

    class Meta:
        # title로 ascending, id로 descending
        ordering = ['title','-id'] 

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + self.last_name

class Album(models.Model):
    # on_delete : 참조하는 테이블이 삭제되는 경우 동작 설정
    # CASCADE : Musician이 삭제되면 같이 삭제
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name

class FieldTest(models.Model):
    fAutoField = models.AutoField(primary_key=True)
    fBigIntegerField = models.BigIntegerField(default=1)
    fBooleanField = models.BooleanField(default=True)
    # max_length는 필수다.
    fCharField = models.CharField(default='charField', max_length=30)
    fDateField = models.DateField(auto_now=False, default=datetime.date.today)
    fDateTimeField = models.DateTimeField(auto_now=False, auto_now_add=False)
    fDecimalField = models.DecimalField(default=1.7321, decimal_places=4, max_digits=10)
    fEmailField = models.EmailField(default="email@example.com")
    fFloatField = models.FloatField(default=1.7321)
    fIntegerField = models.IntegerField(default=10)
    fGenericIPAddressField = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, default=None)
    fNullBooleanField = models.NullBooleanField(default=True)
    fPositiveIntegerField = models.PositiveIntegerField(default=100)
    fPositiveSmallIntegerField = models.PositiveSmallIntegerField(default=50)
    fSlugField = models.SlugField(max_length=30, default='slug')
    fSmallIntegerField = models.SmallIntegerField(default=-50)
    fTextField = models.TextField(default="text text text text text text text")
    fURLField = models.URLField(max_length=200, default='http://localhost')

class Person(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=500, blank=True) # null=False (빈문자 : '')
    bio2 = models.CharField(max_length=500, null=True) # blank=False >> 논리에러(필수칼럼이 됨)
    bio3 = models.CharField(max_length=500, null=True, blank=True) # (빈문자 : NULL)
    birth_date = models.DateField(default=datetime.date.today)

    def contact_default():
        return {"email":"encore@playdata.io"}

    contact_info = JSONField("연락처",
            default=contact_default)

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICE = ((FRESHMAN, '1학년'),
                            (SOPHOMORE, '2학년'),
                            (JUNIOR, '3학년'),
                            (SENIOR, '4학년'))
    year_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICE,
                                default=FRESHMAN)
    
## 1:N 관계 ##
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

# 1:N 관계에서 N측 필드 접근 #

'''
>>> from blog.models import Comment, Post
>>> p = Post.objects.filter(id=7)
>>> p[0].comment_set.all()
>>> Comment.objects.filter(post=post)
'''

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name