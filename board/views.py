from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone

def index(request):
    """
    board 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'board/question_list.html', context)
    return HttpResponse("Wellcome") #홈페이지에 나타날 문구

def detail(request, question_id):
    """
    board 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id) # Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)

def answer_create(request, question_id):
    """
    board 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now())
    return redirect('board:detail', question_id=question.id)
# Create your views here.

