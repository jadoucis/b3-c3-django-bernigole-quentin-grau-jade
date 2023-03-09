from datetime import datetime
from django.db import models
from django.conf import settings


# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'Nom de l\'école : {self.name} - Adresse : {self.address}'


class Reservation(models.Model):
    TIME_CHOICES = (
        ("8h", "8h-9h"),
        ("9h", "9h-10h"),
        ("10h", "10h-11h"),
        ("11h", "11h-12h"),
        ("14h", "14h-15h"),
        ("15h", "15h-16h"),
        ("16h", "16h-17h"),
        ("17h", "17h-18h"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, blank=True)
    time = models.CharField(max_length=50, choices=TIME_CHOICES)

    def __str__(self):
        return f'{self.user} a réservé un créneau le {self.date} à {self.time} pour l école {self.school}'
