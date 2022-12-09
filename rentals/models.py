from django.db import models

class Rental(models.Model):
    name = models.CharField(max_length=64, default='Default rental')

class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()