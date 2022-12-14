from django.db import models

class Rental(models.Model):
    name = models.CharField(max_length=64, default='Default rental')
    def __str__(self):
        return self.name

class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    def __str__(self):
        return f"Rental: {self.rental}, CheckIn: {self.checkin}, CheckOut: {self.checkout}"
