from django.urls import path
import MA_login.views
from . import views

urlpatterns = [
    path('', MA_login.views.home, name='home'),
    path('add_incident/', views.add_incident, name='add_incident'),
    path('knowledge_base/', views.knowledge_base, name='knowledge_base'),
    path('equipment_info/', views.equipment_info, name='equipment_info'),
    path('reports/', views.reports, name='reports'),
    path('add_daily_report/', MA_login.views.add_daily_report,name='add_daily_report')
]
