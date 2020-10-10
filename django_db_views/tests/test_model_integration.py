from django.core.management import call_command
from django.test import TestCase

from .testapp.models import NormalModel, SimpleDjangoDbView

databases = ['postgres', 'sqllite']


def get_tests_class(database: str):
    class DjangoDbViewTest(TestCase):
        databases = [database]

        def test_database_integration(self):
            self.assertIsNotNone(NormalModel.objects.using(database).create())

        def test_makeviewmigrations(self):
            call_command(
                "makeviewmigrations"
            )
            call_command(
                'migrate',
                database=database
            )
            SimpleDjangoDbView.objects.using(database).all()
    return DjangoDbViewTest


for database in databases:
    locals()[f'Test{database}'] = type(f'Test{database}', (get_tests_class(database),), {})
