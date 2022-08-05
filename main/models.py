from django.db import models
from django.urls import reverse


class DailyReport(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(max_length=1500, null=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('home')


class Incident(models.Model):
    techName = models.CharField(max_length=75, null=True)
    location = models.CharField(max_length=50, null=True)
    serialNumber = models.CharField(max_length=50, null=True)
    make = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    gameName = models.CharField(max_length=75, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=50)
    incident = models.TextField(max_length=500, null=True)
    solution = models.TextField(max_length=1500, null=True)

    def __str__(self):
        return self.techName

    def get_absolute_url(self):
        return reverse('incident')
