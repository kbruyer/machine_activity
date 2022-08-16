from django.contrib.auth.decorators import login_required
from django.db.models import Q
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
            'tech_Name': post.tech_Name,
            'location': post.location,
            'serial_Number': post.serial_Number,
            'make': post.make,
            'model': post.model,
            'game_Name': post.game_Name,
            'date': post.date,
            'category': post.category,
            'incident': post.incident,
            'solution': post.solution
        }
        return HttpResponse(template.render(context, request))


@login_required
def knowledge_base(request):
    incident_query_dict = request.GET

    query = incident_query_dict.get('q')

    search_object = None

    if query is not None:
        search_object = Incident.objects.filter(Q(incident__contains=query)).values()
    context = {'incident': search_object}
    return render(request, '../templates/pages/knowledge_base.html', context)


@login_required
def equipment_info(request):
    return render(request, 'pages/equipment_info.html')


@login_required
def daily_activity_report(request):
    query_dict = request.GET

    date_query = query_dict.get('created')
    desc_query = query_dict.get('desc')

    date_search_object = None
    desc_search_object = None

    if date_query is not None:
        date_search_object = DailyReport.objects.filter(Q(created__exact=date_query)).values()
    elif desc_query is not None:
        desc_search_object = DailyReport.objects.filter(Q(description__contains=desc_query)).values()

    context = {'daily_report_date': date_search_object,
               'daily_report_desc': desc_search_object,
               }
    return render(request, '../templates/pages/daily_activity_report.html', context)


@login_required
def slot_machines_report(request):
    query_dict = request.GET

    location_query = query_dict.get('location')
    serial_number_query = query_dict.get('serial_number')
    make_query = query_dict.get('make')
    model_query = query_dict.get('model')
    game_name_query = query_dict.get('game_name')
    date_query = query_dict.get('date')
    category_query = query_dict.get('category')

    location_search_object = None
    serial_number_search_object = None
    make_search_object = None
    model_search_object = None
    game_name_search_object = None
    date_search_object = None
    category_search_object = None

    if location_query is not None:
        location_search_object = Incident.objects.filter(Q(location__exact=location_query)).values()
    elif serial_number_query is not None:
        serial_number_search_object = Incident.objects.filter(Q(serial_Number__exact=serial_number_query)).values()
    elif make_query is not None:
        make_search_object = Incident.objects.filter(Q(make__exact=make_query)).values()
    elif model_query is not None:
        model_search_object = Incident.objects.filter(Q(model__exact=model_query)).values()
    elif game_name_query is not None:
        game_name_search_object = Incident.objects.filter(Q(game_Name__exact=game_name_query)).values()
    elif date_query is not None:
        date_search_object = Incident.objects.filter(Q(date__exact=date_query)).values()
    elif category_query is not None:
        category_search_object = Incident.objects.filter(Q(category__exact=category_query)).values()

    context = {
        'location': location_search_object,
        'serial_number': serial_number_search_object,
        'make': make_search_object,
        'model': model_search_object,
        'game_name': game_name_search_object,
        'date': date_search_object,
        'category': category_search_object
    }
    return render(request, '../templates/pages/slot_machines_report.html', context)


@login_required
def tech_activity_report(request):
    query_dict = request.GET

    tech_query = query_dict.get('tech_name')
    date_query = query_dict.get('date')

    tech_search_object = None
    date_search_object = None

    if tech_query is not None:
        tech_search_object = Incident.objects.filter(Q(tech_Name__contains=tech_query)).values()
    elif date_query is not None:
        date_search_object = Incident.objects.filter(Q(date__exact=date_query)).values()
    context = {
        'tech_name': tech_search_object,
        'date': date_search_object
    }
    return render(request, '../templates/pages/tech_activity_report.html', context)


class DailyReportCreateView(CreateView):
    model = DailyReport
    template_name = 'pages/add_daily_report.html'
    fields = ['description']


class IncidentSolutionCreateView(CreateView):
    model = Incident
    template_name = 'pages/add_incident_solution.html'
    fields = ['tech_Name', 'location', 'serial_Number', 'make', 'model', 'game_Name', 'category', 'incident',
              'solution']


class ReportsTemplateView(TemplateView):
    template_name = 'pages/reports.html'
