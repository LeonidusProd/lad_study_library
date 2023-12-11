from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *

popular_books = [
    {'name': 'Название популярной книги 1', 'author': 'Автор 1', 'foto': '../../static/img/someBook.png'},
    {'name': 'Название популярной книги 2', 'author': 'Автор 2', 'foto': '../../static/img/someBook.png'},
    {'name': 'Название популярной книги 3', 'author': 'Автор 3', 'foto': '../../static/img/someBook.png'},
    {'name': 'Название популярной книги 4', 'author': 'Автор 4', 'foto': '../../static/img/someBook.png'},
    {'name': 'Название популярной книги 5', 'author': 'Автор 5', 'foto': '../../static/img/someBook.png'}
]

def index(request):
    return render(
        request,
        'main/index.html',
        context={
            'pop_books': popular_books,
            'is_login': False,
            'username': ''
        }
    )

def books(request, book_id=0):
    if book_id == 0:
        output = f'<h2>Список всех книг</h2>'
    else:
        output = f'<h2>Детали книги с id={book_id}</h2>'

    return HttpResponse(output)

def add(request):
    output = f'<h2>Форма добавления новой книги</h2>'

    return HttpResponse(output)

def edit(request, book_id):
    output = f'<h2>Форма редактирования информации о книге с id={book_id}</h2>'

    return HttpResponse(output)

def search(request):
    s_input = request.GET.get('search', 'None')

    data = {'search_request': s_input}

    return render(request, 'main/search.html', context=data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def login(request):
    # return render(request, 'main/login.html')

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            print(login_form.cleaned_data)
            return render(request, 'main/index.html', context={'pop_books': popular_books})
        else:
            pass
            # return HttpResponse("Ошибка введённых данных")
    else:
        login_form = LoginForm()
        data = {'form': login_form}
        return render(request, 'main/login.html', context=data)

# def register(request):
#     # reg_form = RegistrationForm()
#     # data = {'form': reg_form}
#     # return render(request, 'main/register.html', context=data)
#
#     if request.method == 'POST':
#         reg_form = RegistrationForm(request.POST)
#         if reg_form.is_valid():
#             # print(reg_form.cleaned_data)
#             new_user = User(
#                 username=reg_form.cleaned_data['username'],
#                 email=reg_form.cleaned_data['email'],
#                 password=reg_form.cleaned_data['password1']
#             )
#             new_user.save()
#             return render(
#                 request,
#                 'main/index.html',
#                 context={
#                     'pop_books': popular_books,
#                     # 'is_login': True,
#                     # 'username': reg_form.cleaned_data['user_name']
#                 }
#             )
#         else:
#             # pass
#             return HttpResponse("Ошибка введённых данных")
#     else:
#         reg_form = RegistrationForm()
#         data = {'form': reg_form}
#         return render(request, 'main/register.html', context=data)

class register(CreateView):
    form_class = RegistrationForm
    template_name = 'main/register.html'
    success_url = '../'