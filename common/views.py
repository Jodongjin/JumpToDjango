from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # form의 입력값을 개별적으로 얻기 위함
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증 (사용자명과 비밀번호 검증)
            login(request, user)  # 로그인 (사용자 세션을 생성)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
