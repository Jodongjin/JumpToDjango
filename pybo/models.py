from django.db import models
from django.contrib.auth.models import User  # views의 함수호출 시 전달하는 request 인자는 로그인 시 User, 로그아웃 시 AnonymousUser 객체를 전달함

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null = True, blank = True)  # blank = True: form.is_valid()를 통한 입력 데이터 검증 시 값이 없는 것을 허용
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')