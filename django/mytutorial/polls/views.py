from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# 클래스 기반 뷰 (View)
# ListView 제너릭뷰는 <app name>/<model name>_list.html 템플릿을 기본으로 사용한다.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # 자동 생성된 컨텍스트 변수를 덮어쓰려면 다음과 같이 선언한다.
    # 자동 생성된 컨텍스트 변수 : question_list
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# DetailView 제너릭 뷰는 URL의 기본 키 값이 'pk' 로 지정돼 있다.
# 템플릿은 <app name>/<model name>_detail.html 템플릿을 사용한다.
# 자동 생성 예시 : polls/question_detail.html
class DetailView(generic.DetailView):
    model = Question
    # 자동 생성된 기본 템플릿 이름 대신 다른 이름을 쓰는 경우 알려줘야 한다.
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def index(request):
    '''
    ## 방법 1 ##
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    '''

    ## 방법 2 ##
    # 템플릿을 불러온 후 컨텍스트를 전달한다.
    # context 는 template 에서 쓰이는 변수명과, Python 의 객체를 연결하는 사전형 값이다.
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    '''

    ## 방법 3 ##
    # 단축기능을 사용해서 작성하기
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# 요청된 질문의 ID 가 없을 경우 Http404 예외를 발생시킨다.
# Http404()로 직접 예외를 발생시킴.
'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
'''

# 단축기능(shortcut : get_object_or_404())으로 작성
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST : 전송된 데이터에 접근할 수 있도록 해주는 객체다.
        # request.POST['choice'] : 선택된 설문의 ID를 문자열로 반환한다.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # POST 데이터에 choice가 없는 경우 KeyError가 발생한다.
    except (KeyError, Choice.DoesNotExist):
        # 에러 메시지와 함께 설문조사 폼을 다시 보여준다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # reverse()함수로 URL을 만들어서 지정 URL로 재전송(Redirect)한다.
        # reverse() 반환 예시 : '/polls/3/results/' (3은 question.id)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))