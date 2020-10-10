from django.db import models

from django_db_views.db_view import DBView


class NormalModel(models.Model):
    name = models.CharField(max_length=15)


class SimpleDjangoDbView(DBView):

    view_definition = """
        SELECT row_number() over () as id;
    """

    class Meta:
        managed = False
        db_table = 'simple_django_db_view'
