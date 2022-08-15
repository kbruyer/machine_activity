from django.db import models
from django.urls import reverse


class DailyReport(models.Model):
    created = models.DateField(auto_now_add=True, null=True)
    description = models.TextField(max_length=1500, null=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('home')


class Incident(models.Model):
    SLOT_MACHINES = 'Slot Machines'
    TABLE_GAMES = 'Table Games'
    CAGE = 'Cage'
    RECYCLER = 'Recycler'
    OTB = 'Off Track Betting'
    BENCH = 'Bench'
    VENDOR = 'Vendor'
    NRT = 'NRT'
    MISC = 'Misc'

    EQUIPMENT_CHOICES = [
        (SLOT_MACHINES, 'Slot Machines'),
        (TABLE_GAMES, 'Table Games'),
        (CAGE, 'Cage'),
        (RECYCLER, 'Recycler'),
        (OTB, 'Off Track Betting'),
        (BENCH, 'Bench'),
        (VENDOR, 'Vendor'),
        (NRT, 'NRT'),
        (MISC, 'Misc')
    ]

    tech_Name = models.CharField(max_length=75, null=True)
    location = models.CharField(max_length=50, null=True)
    serial_Number = models.CharField(max_length=50, null=True)
    make = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    game_Name = models.CharField(max_length=75, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    category = models.CharField(max_length=20, choices=EQUIPMENT_CHOICES, default=SLOT_MACHINES)
    incident = models.TextField(max_length=500, null=True)
    solution = models.TextField(max_length=1500, null=True)

    def __str__(self):
        return self.tech_Name

    def get_absolute_url(self):
        return reverse('incident')
