from django.test import TestCase

class ViewTest(TestCase):

    def test_home_page_url_1(self):

        print('.......... TESTING HOME PAGE URL / ')
        response = self.client.get('/')
        print('Response status code : ' + str(response.status_code))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rentals/index.html')

    def test_home_page_url_2(self):

        print('.......... TESTING HOME PAGE URL /rentals/ ')
        response = self.client.get('/rentals/')
        print('Response status code : ' + str(response.status_code))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rentals/index.html')

