from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question

def index(request):
    page = request.GET.get('page', '1')  # 페이지 (default = 1 -> /pybo/?page=1
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 (icontains: 대소문자 구문 없이 검색)
            Q(content__icontains=kw) |  # 내용
            Q(answer__content__icontains=kw) |  # 답변 내용
            Q(author__username__icontains=kw) |  # 질문 글쓴이
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지 당 10개씩
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # 없는 question_id일 경우, 404 error
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)  # id에 해당되는 question 객체와 detail html을 랜더링