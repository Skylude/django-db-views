from django.db import models


class NormalModel(models.Model):
    name = models.CharField(max_length=15)
