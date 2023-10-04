from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):  # UserCreationForm을 그대로 사용해도 되지만, email 등의 필드를 추가하기 위해 상속하여 구현
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
# 상속한 UserCreationForm의 is_valid 함수는 username, password1, password2가 모두 입력되었는지, 비밀번호 값이 같은지, 생성 규칙에 맞는지 등을 검사