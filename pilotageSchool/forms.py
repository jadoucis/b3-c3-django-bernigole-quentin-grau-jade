from django import forms


# Logging form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, label='Nom d\'utilisateur')
    password = forms.CharField(max_length=200, widget=forms.PasswordInput ,label='Mot de passe')