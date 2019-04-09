from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    # 장고에서 제공하는 모델의 입력 폼을 쉽게 만들 수 있다.
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    # "clean_필드명" 형태의 메서드.
    # 각 필드의 clean 메서드가 호출된 후에 호출되는 메서드이다.
    # 특별한 유효성 검사나 조작을 하고 싶을 때 사용한다.
    def clean_password2(self):
        # 반드시 cleaned_data에서 필드 값을 찾아서 사용해야 한다.
        cd = self.cleaned_data
        
        # password와 password2가 같은지 비교한다.
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']