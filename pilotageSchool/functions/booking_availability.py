from datetime import datetime, timedelta
from ..models import Reservation, School


def validWeekday(days):
    # Loop to select bookable days in the next 15 days
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    weekdays = []
    for i in range(0, days):
        x = tomorrow + timedelta(days=i)
        y = x.strftime('%A')
        if y in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    # Check that the days are not complete
    validateWeekdays = []
    for j in x:
        if Reservation.objects.filter(date=j).count() < 8:
            validateWeekdays.append(j)
    return validateWeekdays


def isTimeValid(day, time):
    # Check that the times are not complete
    x = []
    for k in time:
        if Reservation.objects.filter(date=day, time=k).count() < 1:
            x.append(k)
    return x
