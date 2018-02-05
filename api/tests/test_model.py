from django.test import TestCase
from client_api.models import Create
import datetime


class toDoApiModelTest(TestCase):

    def setUp(self):
        self.obj = toDo(
            Description='comprar pão',
            Date=datetime.date(2018, 1, 2),
            Status='pendente'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Create.objects.exists())
