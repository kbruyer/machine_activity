from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from .forms import LoginForm
from .models import DailyReport, Incident


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled main')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


class HomeListlView(ListView):
    model = DailyReport
    template_name = 'pages/home.html'


class DailyReportCreateView(CreateView):
    model = DailyReport
    template_name = 'pages/add_daily_report.html'
    fields = ['description']


class IncidentSolutionTemplateView(TemplateView):
    template_name = 'pages/incident_solution.html'


class IncidentSolutionCreateView(CreateView):
    model = Incident
    template_name = 'pages/add_incident_solution.html'
    fields = ['techName', 'location', 'serialNumber', 'make', 'model', 'gameName', 'category', 'description', 'notes',
              'solution']


class KnowledgeBaseTemplateView(TemplateView):
    template_name = 'pages/knowledge_base.html'


class EquipmentInfoTemplateView(TemplateView):
    template_name = 'pages/equipment_info.html'


class ReportsTemplateView(TemplateView):
    template_name = 'pages/reports.html'
