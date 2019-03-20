from django import forms
from .models import Book

def minlength3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상입니다.")

class BookForm(forms.Form):
    title = forms.CharField(label="form 제목")
    author = forms.CharField(label="form 저자", validators=[minlength3_validator])
    publisher = forms.CharField(label="form 출판사", required=False)

    
    def save2(self, commit=True):
        book = Book(**self.cleaned_data)
        if commit:
            book.save()
        return book
    