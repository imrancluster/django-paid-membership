from django.test import TestCase


class MyPublicationTests(TestCase):
    def test_home(self):
        response = self.client.get('http://localhost:8087')
        self.assertEqual(response.status_code, 200)

