from django.db import models
from django.shortcuts import reverse
from django import forms
from django.core.validators import MinLengthValidator

def minlength5_validator(value):
    if len(value) < 5:
        raise forms.ValidationError('5자리 이상만 입력가능!')


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    publisher = models.CharField(max_length=50, validators=[minlength5_validator])
    publication_date = models.DateField(auto_now_add=True)
    ip = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)
    photo2 = models.ImageField(blank=True, upload_to='book')
    photo3 = models.ImageField(blank=True, upload_to='book/%Y/%m/%d')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
		# return reverse("book:list")
        return reverse("book:detail", kwargs={"pk": self.id})


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'photo', 'photo2', 'photo3']
        labels = {'title':'ModelForm 제목', 'author':'ModelForm 저자',
                'publisher':'ModelForm 출판사'}
        help_texts = {'author':'작가이름을 3자리 이상으로 입력하세요.',
                'ip':'IP주소는 자동으로 들어갑니다.'}
