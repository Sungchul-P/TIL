from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from .models import Article
from django.http import HttpResponse
from django.db.models import Q
from django.template.loader import render_to_string
from django.urls.base import reverse
from django.utils import timezone

class Person():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return self.name + " 안녕하세요~~"
# ----------------------------------------------- #

# [ FormView ]

from .forms import ContactForm
from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = 'shop/contact.html'
    form_class = ContactForm
    success_url = '/shop/thanks' # urls.py
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data)
        form.send_email()
        return super().form_valid(form)

def success(request):
    return render(request, 'shop/success.html')

# ----------------------------------------------- #

# [ CreateView, UpdateView, DeleteView ]

from django.views.generic.edit import CreateView, UpdateView, DeleteView

article_new = CreateView.as_view(model=Article, fields='__all__')

article_edit = UpdateView.as_view(model=Article, fields='__all__')

article_del = DeleteView.as_view(model=Article, success_url='/shop/')

# ----------------------------------------------- #

def template_test(request):
    article = Article.objects.get(id=1)
    myname = '성철'
    people = ['정표','왕기','아라']
    p = Person('정은')

    dt = timezone.now()
    str_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
    past_dt = timezone.datetime(2018,10,22)
    future_dt = timezone.datetime(2019,5,21)

    return render(request, 'shop/template_test.html', 
                {'article':article, 'first_name':myname, 'people':people, 'person':p,
                'student_list':['std1', 'std2'], 'datetime_obj':dt,
                'dt':dt, 'sdt':str_dt, 'past_dt':past_dt, 'future_dt':future_dt,
                'value':[], 'value2':None, 'value3':['a','b','c']})

# ----------------------------------------------- #
'''
def article_list(request):
    qs = Article.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__contains=q)
    return render(request, 'shop/article_list.html',
            {'article_list':qs, 'q2':q})
'''
from django.views.generic import ListView
# article_list = ListView.as_view(model=Article, paginate_by=10)

class ArticleListView(ListView):
    model = Article
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mymessage"] = "ListView 상속"
        context["today"] = timezone.now()
        return context

article_list = ArticleListView.as_view()
    

# ----------------------------------------------- #

def article_insert(request):
    article = Article(title='목요일', body='날씨가 더 좋아요', status='p')
    article.save()
    Article.objects.create(title='금요일', body='날씨가 더 좋아요', status='p')
    return HttpResponse("입력합니다.")
    # return redirect('/shop')

def article_update(request):
    ''' 
    # 특정 대상 한 건만 수정하기 #
    article = Article.objects.first()
    article.title = '업데이트 금요일입니다.'
    article.save()
    
    # 조건에 해당되는 데이터 수정하기 #
    article_qs = Article.objects.filter(title__contains="일")
    for article in article_qs:
        article.title = "일 => 변경완료!"
        article.save()
    '''

    article_qs = Article.objects.filter(title__contains="일")
    article_qs.update(title="미숫가루!")
    print(article_qs.query)
    
    return HttpResponse("수정합니다.")

def article_delete(request):
    # title에 4 또는 6이 포함된것은 모두 삭제
    article_qs = Article.objects.filter(Q(title__contains="4") | Q(title__contains="6"))
    article_qs.delete()
    return HttpResponse("삭제합니다.")


def article_detail(request, id):
    # instance = Article.objects.get(id=id)
    instance = get_object_or_404(Article, id=id)
    # print(instance)
    return render(request, 'shop/article_detail.html', {'article':instance})

# ----------------------------------------------- #

# article_detail() 함수를 다르게 정의해 보자.
# 하나의 틀을 만들어 놓고, 여러 모델에 적용할 수 있도록 한다.
def generate_view_fn(model):
    def view_fn(request, id):
        instance = get_object_or_404(model, id=id)
        instance_name = model._meta.model_name
        print('instance_name : ', instance_name)
        print('app_name : ', model._meta.app_label)

        template_name = '{}/{}_detail2.html'.format(model._meta.app_label, instance_name)
        print('template_name : ', template_name)

        return render(request, template_name, {instance_name:instance, })

    return view_fn

# article_detail = generate_view_fn(Article)

# ----------------------------------------------- #

# 클래스 기반 뷰 (Class-based View; CBV)
'''
class DetailView:
    def __init__(self, model):
        self.model = model

    def get_object(self, *args, **kwargs):
        return get_object_or_404(self.model, id=kwargs["id"])

    def get_template_name(self):
        instance_name = self.model._meta.model_name
        template_name = '{}/{}_detail2.html'.format(self.model._meta.app_label, instance_name)
        return template_name

    def dispatch(self, request, *args, **kwargs):
        instance_name = self.model._meta.model_name
        return render(request, self.get_template_name(), 
                {instance_name:self.get_object(*args, **kwargs)})

    @classmethod
    def as_view(cls, model):

        def view(request, *args, **kwargs):
            self = cls(model) # 모델 생성
            return self.dispatch(request, *args, **kwargs)

        return view

article_detail = DetailView.as_view(Article)
'''
from django.views.generic import DetailView

article_detail = DetailView.as_view(model=Article)

class ArticleDV(DetailView):
    model = Article

article_detail = ArticleDV.as_view()

# ----------------------------------------------- #

from django.views import View
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("MyView의 get 메서드")

# ----------------------------------------------- #

from django.views.generic.base import TemplateView
class HomePageView(TemplateView):
    template_name = 'shop/home.html'
    
    # get_context_data() 재정의
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_list5"] = Article.objects.all()[:5]
        context["mymessage"] = "벌써 금요일 :("
        return context

# ----------------------------------------------- #

def article_reversetest(request):
    a = reverse('shop:list')
    print('shop:list와 같이 요청함: ', a)

    a = reverse('shop:detail', args=[1]) # '<id>/detail' => '1/detail'
    print('shop:detail과 같이 요청함: ', a)

    a = reverse('shop:detail', kwargs={'id':2}) # '<id>/detail' => '2/detail'
    print('shop:detail과 같이 요청함: ', a)

    a = reverse('shop:detail', 3) # '<id>/detail' => '3/detail'
    print('shop:detail과 같이 요청함: ', a)

    return redirect(a)
    # return redirect('shop:list')

def test1(request):
    response = render(request, 'shop/test1.html', {'mymessage':'render이용하기'})
    return response

def test2(request):
    s = render_to_string('shop/test1.html', {'mymessage':'render_to_string이용하기'})
    return HttpResponse(s)

def test3(request):
    if request.method == "GET":
        response = render(request, 'shop/csrf_input.html')
        return response
    else:
        title = request.POST['title']
        body = request.POST['body']
        status = request.POST['status']
        aa = Article(title=title, body=body, status=status)
        aa.save()
        return HttpResponse("입력합니다.")

def test4(request):
    author = request.POST['author']
    # response = render(request, 'shop/csrf_input.html')
    return HttpResponse(author)