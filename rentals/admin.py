from django.contrib import admin
from .models import Rental
from .models import Reservation

# Register your models here.

admin.site.register(Rental)
admin.site.register(Reservation)
