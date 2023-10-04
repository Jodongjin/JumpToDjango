from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):  # forms.Form, forms.ModelForm이 있음. ModelForm은 모델과 연결된 폼(폼을 저장하면 연결된 모델의 데이터를 저장) -> Meta 이너 클래스 필수
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        # widgets = {  # Form에 적용할 스타일
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.TextInput(attrs={'class': 'form-control', 'rows': 10})
        # }
        labels = {
            'subject': '제목',
            'content': '내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용'
        }