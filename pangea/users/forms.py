from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'login_form', 'style': 'margin-bottom: 30px', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'login_form', 'style': 'margin-bottom: 15px', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'login_form', 'style': 'margin-bottom: 14px', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'login_form', 'style': 'margin-bottom: 14px', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'login_form', 'style': 'margin-bottom: 14px', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'login_form', 'style': 'margin-bottom: 14px', 'placeholder': 'Введите адрес эл. почты'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'type': 'tel', 'class': 'login_form', 'style': 'margin-bottom: 14px', 'placeholder': 'Введите номер телефона'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'login_form', 'style': 'margin-bottom: 14px', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'login_form', 'style': 'margin-bottom: 14px', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'form-control py-2'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-custom w-100 p-2 border rounded '
                                                                      'bg-dark-subtle', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-custom w-100 p-2 border rounded '
                                                                   'bg-dark-subtle', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'image', 'username', 'email')
