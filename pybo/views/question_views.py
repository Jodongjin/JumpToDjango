from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':  # '저장하기' 눌렀을 때
        form = QuestionForm(request.POST)  # 사용자가 입력한 정보로 form 생성
        if form.is_valid():
            question = form.save(commit=False)  # 임시 저장하여 question 객체 리턴
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시 설정 (데이터 저장 시점에 생성해야 하는 값이므로 QuestionFrom을 통한 등록 x)
            question.save()  # 데이터 실제 저장
            return redirect('pybo:index')
    else:  # '질문 등록하기' 눌렀을 때(GET) -> 등록 화면으로 이동
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id = question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        question = form.save(commit = False)
        question.modify_date = timezone.now()  # 수정일시 저장
        question.save()
        return redirect('pybo:detail', question_id = question_id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question_id)
    question.delete()
    return redirect('pybo:index')

@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question_id)