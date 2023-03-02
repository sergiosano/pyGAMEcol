from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,min_length=4, max_length=20, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'username'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'id': 'email'}))
    password = forms.CharField(required=True, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'id': 'password'}))
    passwordrpt = forms.CharField(required=True, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'id': 'passwordrpt'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuario previamente registrado.')
        
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Correo electrónico previamente registrado.')
        
        return email

    def clean_passwordrpt(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('passwordrpt') != cleaned_data.get('password'):
            raise forms.ValidationError('Las contraseñas no coinciden.')
    
    def save(self):
        return User.objects.create_user(self.cleaned_data.get('username'), self.cleaned_data.get('email'), self.cleaned_data.get('password'))