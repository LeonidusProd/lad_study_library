from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # URL адреса входа и выхода
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),

    path('register/', views.register, name='register'),

    path('user/', views.personal_cab, name='personalCab'),
    path('', views.index, name='index'),
]

# urlpatterns = [
#     path('search/', views.search),
#     re_path(r'^books/book/(?P<book_id>\d+)', views.book_page),
#     re_path(r'^books/', views.books),
#     path('about/', views.about),
#     path('contact/', views.contact),
#     path('login/', views.login.as_view()),
#     path('logout/', views.logout_user),
#
#
#     path('books/', views.books),
#     path('add/', views.add),
#
# ]