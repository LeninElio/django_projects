from django import forms
from django.contrib.auth.models import User


class Registro(forms.Form):
    """
    Formulario de registro de usuarios.
    """
    username = forms.CharField(
        min_length=4,
        max_length=100,
        required=True,
        label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'username',
            'placeholder': 'Nombre de usuario'
        }))
    email = forms.EmailField(
        required=True,
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Correo electrónico'
        }))
    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'password',
            'placeholder': 'Contraseña'
        }))

    password_confirm = forms.CharField(
        required=True,
        label='Repita la contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'password',
            'placeholder': 'Contraseña'
        }))


    def clean_username(self):
        """
        Validamos que el usuario no exista.
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya existe')
        return username


    def clean_email(self):
        """
        Validamos que el correo no exista.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya existe')
        return email


    def clean(self):
        """
        Validamos que las contraseñas sean iguales.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return cleaned_data

    def save(self):
        """
        Guardamos el usuario con los datos validados.
        """
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
