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

class PreviousReservation(models.Model):
    rental_name = models.CharField(max_length=64, default='Default rental')
    reservation_id = models.IntegerField(primary_key=True)
    reservation_checkin = models.DateField()
    reservation_checkout = models.DateField()
    previous_reservation_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'rentals_previous_reservation'
