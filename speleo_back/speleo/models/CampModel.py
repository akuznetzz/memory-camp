from django.db import models


class CampModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    region = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    # participants = models.ManyToManyField()
