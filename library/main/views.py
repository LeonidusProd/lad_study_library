from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
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

def books(request):
    books = Book.objects.all()
    paginator = Paginator(books, 16)

    page = request.GET.get("page")

    book_list = []
    page_obj = paginator.get_page(page)
    for book in page_obj:
        book_list.append(
            {
                'id': book.pk,
                'title': book.name,
                'author': book.author.__str__(),
                'cover': book.foto
            }
        )

    data = {
        'book_list': book_list,
        'page_obj': page_obj
    }

    return render(
        request,
        'main/catalog.html',
        context=data
    )

    # if page == 0:
    #     book_list = []
    #     for book in Book.objects.all():
    #         book_list.append(
    #             {
    #                 'title': book.name,
    #                 'author': book.author.__str__(),
    #                 'cover': book.foto
    #             }
    #         )
    #
    #     data = {
    #         'book_list': paginator.get_page(page_number)
    #     }
    #
    #     return render(
    #         request,
    #         'main/catalog.html',
    #         context=data
    #     )
    # else:
    #     return render(request, 'main/catalog.html')

def add(request):
    output = f'<h2>Форма добавления новой книги</h2>'

    return HttpResponse(output)

def book_page(request, book_id):
    if request.user.is_authenticated:
        print('____________Пользователь авторизован')
        user_read_obj = User_Reading.objects.filter(user=request.user.pk)
        user_read_books = [rb.book.pk for rb in user_read_obj]
        print(f'____________{book_id}')
        print(f'____________{user_read_books}')
        if int(book_id) in user_read_books:
            print('____________Книга в списке')
            inReadList = True
        else:
            print('____________Книга не в списке')
            inReadList = False
    else:
        print('____________Пользователь не авторизован')
        inReadList = False


    if request.method == 'POST':
        if 'addToReadList' in request.POST:
            print('addToReadList')
            inReadList = True
        if 'deleteFromReadList' in request.POST:
            print('deleteFromReadList')
            inReadList = False
        if 'share' in request.POST:
            print('share')



    book = Book.objects.get(pk=book_id)

    book_genries = Book_Genre.objects.filter(book=book_id)
    genries = ''

    for genr in book_genries:
        genries += f'{genr.genre.name}, '



    book_info = {
        'name': book.name,
        'author': book.author.__str__(),
        'publication_year': book.publication_year,
        'publisher': book.publisher,
        'isbn': book.isbn,
        'foto': book.foto,
        'genries': genries.strip(', ')
    }

    data = {
        'book': book_info,
        'inReadList': inReadList
    }

    return render(
        request,
        'main/bookPage.html',
        context=data
    )

def search(request):
    s_input = request.GET.get('search', 'None')

    data = {'search_request': s_input}

    return render(request, 'main/search.html', context=data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

# def login(request):
#     # return render(request, 'main/login.html')
#
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             print(login_form.cleaned_data)
#             return render(request, 'main/index.html', context={'pop_books': popular_books})
#         else:
#             pass
#             # return HttpResponse("Ошибка введённых данных")
#     else:
#         login_form = LoginForm()
#         data = {'form': login_form}
#         return render(request, 'main/login.html', context=data)


def register(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password1'])
            new_user.save()
            # Создать профиль пользователя, если нужно
            # Profile.objects.create(user=new_user)
            return redirect('login')
    else:
        reg_form = RegistrationForm()
    data = {'form': reg_form}
    return render(request, 'main/reg_log/register.html', context=data)

# class register(CreateView):
#     form_class = RegistrationForm
#     template_name = 'main/register.html'
#     success_url = '../login'

# class login(LoginView):
#     form_class = LoginForm
#     template_name = 'main/login.html'
#
#     def get_success_url(self):
#         return '../books/?page=1'

# def logout_user(request):
#     logout(request)
#     return redirect('../login')

@login_required
def personal_cab(request):
    if request.method == 'POST':
        form = UserInfo(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=request.user.pk)
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()

            return render(
                request,
                'main/personalCab.html',
                context=create_user_data(request, form)
            )
        else:
            return HttpResponse("Ошибка введённых данных")
    else:
        form = UserInfo(initial={
            'username': request.user.username,
            'email': request.user.email
        })

        return render(
            request,
            'main/personalCab.html',
            context=create_user_data(request, form)
        )

def create_user_data(request, form):
    # form = UserInfo(initial={
    #     'username': request.user.username,
    #     'email': request.user.email
    # })

    reading_list = []
    user_reading_list = User_Reading.objects.filter(user=request.user.pk)
    for book in user_reading_list:
        reading_list.append(
            {
                'id': book.book.pk,
                'name': book.book.name,
                'author': book.book.author,
                'foto': book.book.foto
            }
        )

    return {
        'form': form,
        'reading_list': reading_list
    }