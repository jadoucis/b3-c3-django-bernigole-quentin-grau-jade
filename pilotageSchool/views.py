from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from . import forms
from django.shortcuts import render
from .models import School, Reservation
from .forms import RegisterForm
from datetime import datetime, timedelta
from pilotageSchool.functions.booking_availability import check_availability


# Create your views here.

# Main page view
def index(request):
    schools = School.objects.all()
    return render(request, 'templates/school_list.html', {'schools': schools})


# Reservation page view
def reservations_pages(request):
    reservations = Reservation.objects.all()
    return render(request, 'templates/reservations.html', {'reservations': reservations})


# Choose reservation page view
def choose_reservation(request, school_name):
    school = School.objects.filter(name=school_name)
    print(School)
    reservations = Reservation.objects.all()
    weekdays = validWeekday(15)
    validateWeekdays = isWeekdayValid(weekdays)
    time = ["8h", "9h", "10h", "11h", "14h", "15h", "16h", "17h"]
    unavailable_schools = []
    unavailable_date = []
    unavailable_time = []
    for reservation in reservations:
        if check_availability(reservation.school, reservation.date, reservation.time):
            unavailable_date.append(reservation.date)
            unavailable_time.append(reservation.time)
    unavailable_schools.append(unavailable_date)
    unavailable_schools.append(unavailable_time)
    for day in validateWeekdays:
        times = isTimeValid(day, time)
    # if len(unavailable_schools) > 0:
    #     isTimeValid(unavailable_school[0], unavailable_school[1])
    #     # for i in range(0, len(unavailable_schools)):
    #     #     # isTimeValid(unavailable_school[0], unavailable_school[1])
    #     #     # keys = list(unavailable_school)
    #     #     print(unavailable_schools[i][i], unavailable_schools[i+1][i+1])
    # else:
    # if request.method == 'POST':
    #     booking = Reservation.objects.create(
    #         user=request.user,
    #         school=school,
    #         time=request.POST.get("time"),
    #         date=request.session.get('day'),
    #     )
    #     booking.save()
    #     return redirect("Reservations")
    # else:
    return render(request, 'templates/choose_reservation.html',
                      {'school_name': school_name, 'weekdays': weekdays, 'validateWeekdays': validateWeekdays,
                       'times': times})


def validWeekday(days):
    # Boucle pour sélectionner les jours réservable dans les 15 prochains jours
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
            weekdays.append(x.strftime('%Y-%m-%d'))
        print(weekdays)
    return weekdays


def isWeekdayValid(x):
    # Vérifie que les jours ne soient pas complets
    validateWeekdays = []
    for j in x:
        if Reservation.objects.filter(date=j).count() < 8:
            validateWeekdays.append(j)
    return validateWeekdays


def isTimeValid(day, time):
    # Vérifie que les jours ne soient pas complets
    x = []
    for k in time:
        if Reservation.objects.filter(date=day, time=k).count() < 1:
            x.append(k)
    return x


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
