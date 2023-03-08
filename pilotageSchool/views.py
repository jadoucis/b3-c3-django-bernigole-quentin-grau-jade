from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from . import forms
from .models import School
from .forms import RegisterForm

# Create your views here.

# Main page view
def index(request):
    return render(request, "index.html")


# Register view (Bonus)
def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, f"Inscription validée. Vous êtes connecté sous {username}")
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {
        'form':form})

# Login view
def login_page(request):
    form = forms.LoginForm()
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f"Bonjour {user.username}, vous êtes connecté !")
            else:
                messages.info(request, f"Echec de la connexion")
    return render(request, 'login.html', context={'form' : form})

# Logout view
@login_required
def logout_page(request):
    logout(request)
    messages.info(request, "Vous êtes déconnecté.")
    return redirect("index")

def schoolList(request):
    schools = School.objects.all()
    return render(request, 'schoolList.html', {'schools': schools})