from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        min_length=4,
        max_length=50,
        label='Имя пользователя',
        label_suffix='',
        widget=forms.TextInput(attrs={'placeholder': 'Придумайте имя пользователя', 'id': 'username'}),

    )
    email = forms.CharField(
        min_length=5,
        label='Email',
        label_suffix='',
        widget=forms.EmailInput(attrs={'placeholder': 'Укажите вашу электронную почту', 'id': 'email'})
    )

    password1 = forms.CharField(
        min_length=5,
        label='Пароль',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте пароль', 'id': 'password'})
    )

    password2 = forms.CharField(
        min_length=5,
        label='Повтор пароля',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'id': 'password_rep'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError(' Email already in use.')
        return data


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        min_length=4,
        max_length=50,
        label='Имя пользователя',
        label_suffix='',
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя', 'id': 'username'}),

    )

    password = forms.CharField(
        min_length=5,
        label='Пароль',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'id': 'password'})
    )


class UserEditForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError(' Email already in use.')
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['foto']
        widgets = {
            'foto': forms.FileInput(attrs={'class': 'inputfile'}),
        }
        labels = {
            'foto': 'Фото профиля'
        }


class BookShareForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label='Имя отправителя',
        label_suffix='',
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя отправителя', 'id': 'name'})
    )
    email_to = forms.CharField(
        min_length=5,
        label='Почта получателя',
        label_suffix='',
        widget=forms.EmailInput(attrs={'placeholder': 'Укажите электронную почту получателя', 'id': 'email'})
    )
    comment = forms.CharField(
        label='Комментарий',
        label_suffix='',
        widget=forms.Textarea(attrs={'placeholder': 'Комментарий (по желанию)', 'id': 'email'}),
        required=False
    )
