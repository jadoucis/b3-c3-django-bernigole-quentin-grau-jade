import datetime
from django.db import models

# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    def __str__(self):
        return f'Nom de l\'école : {self.name} - Adresse : {self.adress}'

class Reservation(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    className = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField()
    heureDebut = models.TimeField()
    heureFin = models.TimeField()
    isReserved = models.BooleanField(default=False)
    def __str__(self):
        return f'Nom de l\'école : {self.schoolName} - Intitulé du cours : {self.className} - Date du cours : {self.date} - Heure début cours : {self.heureDebut} - Est-il réservé : {self.isReserved}'