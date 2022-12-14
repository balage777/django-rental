from django.test import TestCase
from rentals.models import Rental
from rentals.models import Reservation
from rentals.views import *

class ViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        print('... SETUP TEST DATA ')
        r1 = Rental()
        r1.name  = "rental-1"
        r1.save()

        r2 = Rental()
        r2.name  = "rental-2"
        r2.save()

        res1 = Reservation()
        res1.rental = r1
        res1.checkin = "2022-01-01"
        res1.checkout = "2022-01-13"
        res1.save()

        res2 = Reservation()
        res2.rental = r1
        res2.checkin = "2022-01-20"
        res2.checkout = "2022-02-10"
        res2.save()

        res3 = Reservation()
        res3.rental = r1
        res3.checkin = "2022-02-20"
        res3.checkout = "2022-03-10"
        res3.save()

        res4 = Reservation()
        res4.rental = r2
        res4.checkin = "2022-01-02"
        res4.checkout = "2022-01-20"
        res4.save()

        res5 = Reservation()
        res5.rental = r2
        res5.checkin = "2022-01-20"
        res5.checkout = "2022-02-11"
        res5.save()

    def test_home_page_url_1(self):

        print('... TESTING HOME PAGE URL / ')
        response = self.client.get('/')
        print('...... Response status code : ' + str(response.status_code))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rentals/index.html')

    def test_home_page_url_2(self):

        print('... TESTING HOME PAGE URL /rentals/ ')
        response = self.client.get('/rentals/')
        print('...... Response status code : ' + str(response.status_code))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rentals/index.html')

    def test_previous_reservation(self):

        def check_previous_none(r, rs):
            print("......... Previous reservation ID is None, so this Checkin date should be the least")
            for rr in rs:
                if rr['checkin'] < r['checkin']:
                    print(f"............ Failed: {rr['checkin']} is smaller than {r['checkin']}")
                    return False
                else:
                    print(f"............ Ok: {rr['checkin']} is not smaller than {r['checkin']}")
            return True

        def check_previous(r, rs):
            print("......... Previous reservation ID is not None, so the Checkin date belongs to this previous reservation ID should be samller than the actual Checkin date but bigger all of the others")
            previous = rs[0]
            for rr in rs:
                if rr['checkin'] > previous['checkin'] and rr['checkin'] < r['checkin']:
                    previous = rr
            if previous['id'] is not r['previous']:
                return False
            return True

        print('... TESTING PREVIOUS RESERVATION ID ')

        all_reservations = get_reservations()

        d = dict()
        r = dict()

        for res in all_reservations:
            r[res[1]] = res
            if res[0] in d.keys():
                d[res[0]].append({
                    'rental': res[0],
                    'id': res[1],
                    'checkin': res[2],
                    'checkout': res[3],
                    'previous': res[4]
                })
            else:
                d[res[0]] = [{
                    'rental': res[0],
                    'id': res[1],
                    'checkin': res[2],
                    'checkout': res[3],
                    'previous': res[4]
                }]

        rentals = Rental.objects.all()

        for rental in rentals:
            print(f"...... Testing reservations in {rental}")
            for res in d[rental.name]:
                if res['previous'] is not None:
                    self.assertEqual(check_previous(res, d[rental.name]), True)
                else:
                    self.assertEqual(check_previous_none(res, d[rental.name]), True)


