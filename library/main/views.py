from django.shortcuts import render
from django.http import HttpResponse


popular_books = [
    {'name': 'Название популярной книги 1', 'author': 'Автор 1', 'foto': '../../static/img/someBook.png'},
    {'name': 'Название популярной книги 2', 'author': 'Автор 2', 'foto': '../../static/img/someBook.png'},
    {'name': 'Название популярной книги 3', 'author': 'Автор 3', 'foto': '../../static/img/someBook.png'},
    {'name': 'Название популярной книги 4', 'author': 'Автор 4', 'foto': '../../static/img/someBook.png'},
    {'name': 'Название популярной книги 5', 'author': 'Автор 5', 'foto': '../../static/img/someBook.png'}
]

def index(request):
    return render(request, 'main/index.html', context={'pop_books': popular_books})

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
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def what():
    pass