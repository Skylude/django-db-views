from django.test import TestCase

from .testapp.models import NormalModel


class ModelIntegrationTests(TestCase):
    # databases = ['default', 'postgresql']
    databases = ['default']


    def test_model_without_pg_fields(self):
        self.assertIsNotNone(NormalModel.objects.create())

    # def test_model_with_pg_fields(self):
    #     self.assertIsNotNone(ModelWithPgFields.objects.create())
