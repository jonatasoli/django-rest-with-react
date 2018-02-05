from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
import datetime


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/api/')
        self.week = self.client.get('/api/listweek/')
        self.done = self.client.get('/api/listdone/')
        self.late = self.client.get('/api/listlate/')
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)
        self.assertEqual(200, self.week.status_code)
        self.assertEqual(200, self.done.status_code)
        self.assertEqual(200, self.late.status_code)

    def test_post(self):
        """Post /api/create must return status - success"""
        request = self.client.post('/api/week/', {
                "Description": "Ir ao mercado",
                "Date": str(Date=datetime.date(2018, 1, 3)),
                "Status": "Pendente"
            },
            format='json'
        )
        self.assertEqual("{'status': 'success'}", str(request.data))
