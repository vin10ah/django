from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm


def index(request):
    question_list = Question.objects.order_by('-create_date') # 질문목록 데이터 얻기, - 기호 붙으면 역순 정렬
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context) # render = HTML 파일로 반환

'''
'pybo/quesrion_list.html' -> 템플릿: HTML과 비슷, 파이썬 데이터를 읽어서 사용할 수 있는 HTML 파일
'''

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # Answer 모델 직접 사용하는 방식 
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()
    
    return redirect('pybo:detail', question_id=question.id)


def question_create(request):
    form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})