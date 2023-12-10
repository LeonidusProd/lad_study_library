from django import forms

class RegistrationForm(forms.Form):
    user_name = forms.CharField(
        min_length=4,
        max_length=50,
        label='Имя пользователя',
        label_suffix='',
        widget=forms.TextInput(attrs={'placeholder': 'Придумайте имя пользователя', 'id': 'username'}),

    )
    user_email = forms.CharField(
        min_length=5,
        label='Email',
        label_suffix='',
        widget=forms.EmailInput(attrs={'placeholder': 'Укажите вашу электронную почту', 'id': 'email'})
    )

    user_password = forms.CharField(
        min_length=5,
        label='Пароль',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте пароль', 'id': 'password'})
    )

    user_password_rep = forms.CharField(
        min_length=5,
        label='Повтор пароля',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'id': 'password_rep'})
    )

class LoginForm(forms.Form):
    user_name = forms.CharField(
        min_length=4,
        max_length=50,
        label='Имя пользователя',
        label_suffix='',
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя', 'id': 'username'}),

    )

    user_password = forms.CharField(
        min_length=5,
        label='Пароль',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'id': 'password'})
    )