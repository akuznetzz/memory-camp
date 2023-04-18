from django.db import models
from core import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    nik_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    vk = models.CharField(max_length=100, blank=True, null=True)
    start_education = models.CharField(max_length=100, blank=True, null=True)
    end_education = models.CharField(max_length=100, blank=True, null=True)
    mgri_group = models.CharField(max_length=100, blank=True, null=True)
    speleo_section = models.BooleanField(blank=True, null=True)
    speleo_school = models.BooleanField(blank=True, null=True)
    instructor_list = models.CharField(max_length=1000, blank=True, null=True)
    instructor_key = models.ForeignKey(
        'Profile', on_delete=models.PROTECT, blank=True, null=True)
    group_role = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
