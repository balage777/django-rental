# Generated by Django 4.1.4 on 2022-12-15 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
        """
        DROP VIEW IF EXISTS rentals_previous_reservation;
        CREATE VIEW rentals_previous_reservation AS
        SELECT 
            rentals_rental.name as 'rental_name',
            rentals_reservation.id as 'reservation_id',
            rentals_reservation.checkin as 'reservation_checkin',
            rentals_reservation.checkout as 'reservation_checkout',
            (SELECT id FROM rentals_reservation R 
             WHERE R.rental_id = rentals_rental.id AND R.checkin < rentals_reservation.checkin 
             ORDER BY R.checkin DESC LIMIT 1
            ) as 'previous_reservation_id'
        FROM rentals_reservation 
        LEFT JOIN rentals_rental ON rentals_rental.id=rentals_reservation.rental_id
        ORDER BY rentals_rental.id, rentals_reservation.checkin;
        """            
        ),
    ]
