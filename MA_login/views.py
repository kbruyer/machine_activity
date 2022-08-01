from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import DailyActivityPost


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
                    return HttpResponse('Disabled MA_login')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def home(request):
    post = DailyActivityPost.objects.last()
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
def add_daily_report(request):
    template = loader.get_template('pages/add_daily_report.html')
    return HttpResponse(template.render({}, request))
