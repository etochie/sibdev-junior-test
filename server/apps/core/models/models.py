from django.db import models


class Deal(models.Model):
    customer = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    total = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()
    date = models.DateTimeField()
