import array

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from . import forms
from django.shortcuts import render

from .functions.booking_availability import validWeekday, isWeekdayValid, isTimeValid
from .models import School, Reservation
from .forms import RegisterForm
from datetime import datetime, timedelta


# Create your views here.

# Main page view
def index(request):
    schools = School.objects.all()
    return render(request, 'templates/school_list.html', {'schools': schools})


# Reservation page view
def reservations_pages(request):
    reservations = Reservation.objects.filter(user=request.user)
    if request.method == 'POST':
        booking = Reservation.objects.filter(id=request.POST.get("id"))
        booking.delete()
        messages.success(request, "Votre annulation a été prise en compte!")
        return redirect("Reservations")
    else:
        return render(request, 'templates/reservations.html', {'reservations': reservations})


# Choose reservation page view
def choose_reservation(request, school_name):
    school = School.objects.get(name=school_name)
    weekdays = validWeekday(15)
    validateWeekdays = isWeekdayValid(weekdays, school)
    time = ["8h", "9h", "10h", "11h", "14h", "15h", "16h", "17h"]
    slots = []
    for day in validateWeekdays:
        times = isTimeValid(day, time, school)
        slots.append({
            "day": day,
            'time': times
        })
    if request.method == 'POST':
        print(request.POST.get("time"))
        print(request.POST.get("day"))
        booking = Reservation.objects.create(
            user=request.user,
            school=school,
            time=request.POST.get("time"),
            date=request.POST.get("day"),
        )
        booking.save()
        messages.success(request, "Votre réservation a été prise en compte!")
        return redirect("Reservations")
    else:
        return render(request, 'templates/choose_reservation.html',
                      {'school_name': school_name, 'weekdays': weekdays, 'validateWeekdays': validateWeekdays, 'times': times, 'slots': slots})


# Register view (Bonus)
def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Votre compte a été créé !")
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'templates/register.html', {
        'form': form})


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
                return redirect('index')
            else:
                messages.info(request, f"Echec de la connexion")
    return render(request, 'templates/login.html', context={'form': form})


# Logout view
@login_required
def logout_page(request):
    logout(request)
    messages.info(request, "Vous êtes déconnecté.")
    return redirect("index")
