from datetime import datetime, timedelta
from ..models import Reservation, School


def check_availability(school, date, time):
    avail_list = []
    booking_list = Reservation.objects.filter(school=school)
    for booking in booking_list:
        if booking.date == date and booking.time == time:
            avail_list.append(booking)
    return all(avail_list)
