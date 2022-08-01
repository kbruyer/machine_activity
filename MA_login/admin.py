from django.contrib import admin
from .models import DailyActivityPost


@admin.register(DailyActivityPost)
class PostDailyActivity(admin.ModelAdmin):
    list_display = ('description', 'created')
    list_filter = ('description', 'created')
    search_fields = ('created',)
    ordering = ('created', 'description')
