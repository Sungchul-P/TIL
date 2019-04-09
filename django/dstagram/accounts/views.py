from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        # POST 방식으로 전달된 데이터를 RegisterForm()으로 유효성 검사를 수행한다.
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False) # commit=False : DB 저장 X, 메모리 상에 객체만 생성한다.
            # set_password()를 사용해 비밀번호를 지정한다.(암호화된 상태로 저장됨.)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save() # 실제 데이터베이스에 저장
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        # POST 방식이 아니라면, 입력 폼을 출력한다.
        user_form = RegisterForm()

    # POST 방식이 아닌경우 register 템플릿을 렌더링해 보여준다.
    return render(request, 'registration/register.html', {'form':user_form})