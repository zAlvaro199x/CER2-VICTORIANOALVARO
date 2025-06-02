from django import forms
from django.contrib.auth.models import User
from .models import PerfilUsuario

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de Usuario', max_length=150)
    email = forms.EmailField(label='Correo Electrónico')
    first_name = forms.CharField(label='Nombre', max_length=30)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    direccion = forms.CharField(label='Dirección', max_length=255, required=False)
    telefono = forms.CharField(label='Número de Teléfono', max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email