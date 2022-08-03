from django.db import models
from django.urls import reverse


class DailyReport(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(max_length=1500, null=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('daily_report_detail', args=[str(self.id)])


class Incident(models.Model):
    techName = models.TextField(max_length=75, null=True)
    location = models.TextField(max_length=50, null=True)
    serialNumber = models.TextField(max_length=50, null=True)
    make = models.TextField(max_length=50, null=True)
    model = models.TextField(max_length=50, null=True)
    gameName = models.TextField(max_length=75, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.TextField()
    description = models.TextField(max_length=500, null=True)
    notes = models.TextField(max_length=1500, null=True)
    solution = models.TextField(max_length=1500, null=True)

    def __str__(self):
        return self.techName

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])
