from django.db import models


class CaveModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    coordinates = models.CharField(max_length=255, blank=True, null=True)
    adress = models.CharField(max_length=255, blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
