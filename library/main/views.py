from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
import json

from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages

from library import settings
from .forms import *
from .models import *
import random


def index(request):
    random_books = Book.objects.order_by('?')[:5]

    return render(
        request,
        'main/index.html',
        context={
            'random_books': random_books,
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
        user_read_obj = User_Reading.objects.filter(user=request.user.pk)
        user_read_books = [rb.book.pk for rb in user_read_obj]
        if int(book_id) in user_read_books:
            inReadList = True
        else:
            inReadList = False
    else:
        inReadList = False


    if request.method == 'POST':
        if 'addToReadList' in request.POST:
            if not inReadList:
                user_read_obj = User_Reading(user=request.user, book=Book.objects.get(pk=book_id))
                user_read_obj.save()
                inReadList = True
        if 'deleteFromReadList' in request.POST:
            if inReadList:
                user_read_obj = User_Reading.objects.get(user=request.user, book=Book.objects.get(pk=book_id))
                user_read_obj.delete()
                inReadList = False
        if 'share' in request.POST:
            return redirect('main:book_share', book_id=book_id)
            pass



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


def book_share(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    sent = False

    if request.method == 'POST':
        share_form = BookShareForm(request.POST)

        if share_form.is_valid():
            cd = share_form.cleaned_data
            book_url = request.build_absolute_uri(book.get_absolute_url())
            subject = f"{cd['name']} рекомендует прочитать книгу {book}"
            message = (f"Прочитай книгу {book.author}: {book}.\n\n"
                       f"Вот ссылка: {book_url}.\n\n"
                       f"PS: {cd['comment']}")

            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['email_to']])
            sent = True
    else:
        if request.user.is_authenticated:
            share_form = BookShareForm(initial={'name': request.user.username})
        else:
            share_form = BookShareForm()

    return render(request, 'main/bookShare.html', {'book': book, 'share_form': share_form, 'sent': sent})


def search(request):
    s_input = request.GET.get('search', 'None')

    data = {'search_request': s_input}

    return render(request, 'main/search.html', context=data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


def register(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password1'])
            new_user.save()
            # Создать профиль пользователя, если нужно
            Profile.objects.create(user=new_user)
            return redirect('login')
    else:
        reg_form = RegistrationForm()
    data = {'form': reg_form}
    return render(request, 'main/reg_log/register.html', context=data)

@login_required
def personal_cab(request):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST
        )
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно обновлён')
        else:
            messages.error(request, 'Ошибка обновления профиля')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(
        request,
        'main/personalCab.html',
        context=create_user_data(request, user_form, profile_form)
        )


def create_user_data(request, user_form, profile_form):
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
        'user_form': user_form,
        'profile_form': profile_form,
        'reading_list': reading_list
    }