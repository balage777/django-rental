from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from rentals.models import PreviousReservation

def get_reservations():
    with connection.cursor() as cursor:
        cursor.execute(
        """
        SELECT 
            rentals_rental.name as 'Rental name',
            rentals_reservation.id as 'Reservation ID',
            rentals_reservation.checkin as 'Checkin',
            rentals_reservation.checkout as 'Checkout',
            (SELECT id FROM rentals_reservation R 
             WHERE R.rental_id = rentals_rental.id AND R.checkin < rentals_reservation.checkin 
             ORDER BY R.checkin DESC LIMIT 1
            ) as 'Previous reservation ID'
        FROM rentals_reservation 
        LEFT JOIN rentals_rental ON rentals_rental.id=rentals_reservation.rental_id
        ORDER BY rentals_rental.id, rentals_reservation.checkin
        """
        )
        all = cursor.fetchall()
    return all

def index(request):
    context = {}
    context['previous_reservations'] = PreviousReservation.objects.all()
    return render(request, 'rentals/index.html', context=context)
