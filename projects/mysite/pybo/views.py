from django.shortcuts import render, get_object_or_404
from .models import Question


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