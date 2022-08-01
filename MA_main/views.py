from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def add_incident(request):
    return render(request, 'pages/incident_solution.html', {'section': 'incident'})

@login_required
def knowledge_base(request):
    return render(request, 'pages/knowledge_base.html', {'section': 'knowledge'})

@login_required
def equipment_info(request):
    return render(request, 'pages/equipment_info.html', {'section': 'equipment'})

@login_required
def reports(request):
    return render(request, 'pages/reports.html', {'section': 'reports'})
