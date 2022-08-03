from django.contrib import admin
from .models import DailyReport, Incident


admin.site.register(DailyReport)
admin.site.register(Incident)
