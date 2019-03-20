from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Book, BookModelForm
from .forms import BookForm

class BookListView(ListView):
    model = Book
    paginate_by=5
    template_name='book/list.html'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


# book_list = ListView.as_view(model=Book, template_name='book/list.html')
book_list = BookListView.as_view()
book_detail = DeleteView.as_view(model=Book, template_name='book/detail.html')
# book_new = CreateView.as_view(model=Book, fields='__all__', template_name='book/new_form.html')
book_edit = UpdateView.as_view(model=Book, fields='__all__', template_name='book/edit_form.html')
book_delete = DeleteView.as_view(model=Book, success_url='/book/', template_name='book/confirm_del.html')
'''
def book_edit(request, pk):
    template_name = 'book/edit_form.html'
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.ip = '.'.join(request.META['REMOTE_ADDR'].split('.')[:-1]) + '.99'
            book.save()
            return redirect('/book/')
    else:
        form = BookModelForm(instance=book)

    return render(request, 'book/edit_form.html', {'form':form})
'''

def book_new(request):
    template_name = 'book/new_form.html'
    if request.method == "GET":
        # form = BookForm()
        form = BookModelForm()
    else:
        print("저장한다..")
        # form = BookForm(request.POST, request.FILES)
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():

            # ModelForm - Commit 지연
            book = form.save(commit=False)
            book.ip = request.META['REMOTE_ADDR']
            book.save()
            return redirect(reverse('book:list'))

            # 방법 5
            # Book.objects.create(**form.cleaned_data)
            # return redirect(reverse('book:list'))
            
            '''
            # 방법 4
            Book.objects.create(title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publisher = form.cleaned_data['publisher'])
            return redirect(reverse('book:list'))
            '''
            '''
            # 방법 3
            book = Book(title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publisher = form.cleaned_data['publisher'])
            book.save()
            return redirect(reverse('book:list'))
            '''
            '''
            # 방법 2
            book = Book()
            book.title = form.cleaned_data['title']
            book.author = form.cleaned_data['author']
            book.publisher = form.cleaned_data['publisher']
            book.save()
            return redirect(reverse('book:list'))
            '''
            '''
            # 방법1 
            print("request.POST : ", request.POST)
            print(form)
            print(form.cleaned_data)
            form.save2()
            return redirect(reverse('book:list'))
            '''
    
    return render(request, 'book/new_form.html', {'form':form})

