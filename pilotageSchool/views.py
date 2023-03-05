from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from . import forms

# Create your views here.

# Main page view
def index(request):
    return render(request, "index.html")


# Register view (Bonus)

# Login view