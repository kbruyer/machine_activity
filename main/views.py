from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import LoginForm
from .models import DailyReport, Incident

from django.template import loader


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


@login_required
def home(request):
    post = DailyReport.objects.last()
    if post is None:
        return render(request, '../templates/pages/home.html')
    else:
        template = loader.get_template('../templates/pages/home.html')
        context = {
            'description': post.description,
            'created': post.created
        }
        return HttpResponse(template.render(context, request))


@login_required
def incident_solution(request):
    post = Incident.objects.last()
    if post is None:
        return render(request, '../templates/pages/incident_solution.html')
    else:
        template = loader.get_template('../templates/pages/incident_solution.html')
        context = {
            'techName': post.techName,
            'location': post.location,
            'serialNumber': post.serialNumber,
            'make': post.make,
            'model': post.model,
            'gameName': post.gameName,
            'date': post.date,
            'category': post.category,
            'incident': post.incident,
            'solution': post.solution
        }
        return HttpResponse(template.render(context, request))


class DailyReportCreateView(CreateView):
    model = DailyReport
    template_name = 'pages/add_daily_report.html'
    fields = ['description']


class IncidentSolutionCreateView(CreateView):
    model = Incident
    template_name = 'pages/add_incident_solution.html'
    fields = ['techName', 'location', 'serialNumber', 'make', 'model', 'gameName', 'category', 'incident',
              'solution']


class KnowledgeBaseTemplateView(TemplateView):
    template_name = 'pages/knowledge_base.html'


class EquipmentInfoTemplateView(TemplateView):
    template_name = 'pages/equipment_info.html'


class ReportsTemplateView(TemplateView):
    template_name = 'pages/reports.html'
