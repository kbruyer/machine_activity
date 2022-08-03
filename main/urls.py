from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeListlView, DailyReportCreateView, IncidentSolutionCreateView, IncidentSolutionTemplateView, \
    KnowledgeBaseTemplateView, EquipmentInfoTemplateView, ReportsTemplateView

urlpatterns = [
    # Daily Report Page
    path('', HomeListlView.as_view(), name='home'),
    path('add_daily_report/', DailyReportCreateView.as_view(), name='add_daily_report'),
    path('post/<int:pk>/', HomeListlView.as_view(), name='daily_report_detail'),

    # Incident/Solution Page
    path('incident_solution/', IncidentSolutionTemplateView.as_view(), name='incident'),
    path('add_incident_solution/', IncidentSolutionCreateView.as_view(), name='add_incident_solution'),

    path('knowledge_base/', KnowledgeBaseTemplateView.as_view(), name='knowledge_base'),
    path('equipment_info/', EquipmentInfoTemplateView.as_view(), name='equipment_info'),
    path('reports/', ReportsTemplateView.as_view(), name='reports'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
