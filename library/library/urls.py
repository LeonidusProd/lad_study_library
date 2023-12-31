"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from main import views

urlpatterns = [
    path('search/', views.search, name='search'),
    re_path(r'^books/book/(?P<book_id>\d+)', views.book_page, name='book'),
    re_path(r'^books/', views.books, name='books'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('user/', views.personal_cab, name='user'),
    path('register/', views.register.as_view(), name='register'),
    # path('books/', views.books),
    # path('add/', views.add),
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
]