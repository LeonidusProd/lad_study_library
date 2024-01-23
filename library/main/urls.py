from django.urls import path, re_path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    # URLы входа и выхода
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='main/reg_log/login.html',
            form_class=LoginForm
        ),
        name='login'),
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name='main/reg_log/logout.html'
        ),
        name='logout'
    ),

    # URLы смены пароля
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='main/reg_log/changePW.html',
            success_url=reverse_lazy('personalCab')
        ),
        name='changePW'
    ),
    # Не используется, так как после смены редирект в ЛК
    # path(
    #     'change-password/done/',
    #     auth_views.PasswordChangeDoneView.as_view(template_name='main/reg_log/changePWDone.html'),
    #     name='changePWDone'
    # ),

    # URLы для сброса пароля
    path(
        'reset-password/',
        auth_views.PasswordResetView.as_view(
            template_name='main/reg_log/resetPW.html',
            email_template_name='main/reg_log/resetEmail.html',
            success_url=reverse_lazy('resetPWDone')
        ),
        name='resetPW'
    ),
    path(
        'reset-password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='main/reg_log/resetPWDone.html'
        ),
        name='resetPWDone'
    ),
    path(
        'reset-password/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='main/reg_log/resetPWConfim.html',
            success_url = reverse_lazy('index')
        ),
        name='resetPWConfim'
    ),
    # Не используется, так как после сброса редирект на главную
    # path(
    #     'reset-password/complete/',
    #     auth_views.PasswordResetCompleteView.as_view(template_name='main/reg_log/resetPWComplete.html'),
    #     name='resetPWComplete'
    # ),

    path('register/', views.register, name='register'),

    path('user/', views.personal_cab, name='personalCab'),
    path('books/', views.books, name='books'),
    re_path(r'^books/book/(?P<book_id>\d+)', views.book_page, name='book_page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
]

# urlpatterns = [
#     path('search/', views.search),
#     path('add/', views.add),
# ]