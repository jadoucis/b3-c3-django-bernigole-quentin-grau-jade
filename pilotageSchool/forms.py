from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


# Logging form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, label='Nom d\'utilisateur')
    password = forms.CharField(max_length=200, widget=forms.PasswordInput, label='Mot de passe')


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=200, label='Nom d\'utilisateur', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Rida123'}), )
    email = forms.EmailField(label='Adresse mail', widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'rida.messaoudene@reseau-cd.fr'}))
    first_name = forms.CharField(label='Prénom', max_length=50,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control form-control-lg', 'placeholder': 'Rida'}))
    last_name = forms.CharField(label='Nom de famille', max_length=50,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control form-control-lg', 'placeholder': 'Messaoudene'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'

